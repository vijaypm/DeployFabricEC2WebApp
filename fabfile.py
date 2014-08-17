__author__ = 'vijay'
from fabric.api import env, local, run, execute, cd, put
from fabric.state import connections
import LaunchEC2
import TerminateEC2
import CleanEC2Security
import defaults
import time
import logging
import os

logging.getLogger('boto').setLevel(logging.CRITICAL)

#env.hosts = []
env.user = defaults.EC2_USER
env.key_filename = defaults.KEY_PATH
env.connection_attempts = 3

def local_uname():
    local('uname -a')

def remote_uname():
    run('uname -a')

def test_task(instance_ip, option_arg=None):
    print env.host_string
    print env.instance_ip[env.host]
    if instance_ip is None:
        raise Exception('Instance IP argument is None')
    print instance_ip
    print option_arg

def test_execute(option_arg=None):
    ip_address = '127.0.0.1'
    dns_name = 'localhost'
    env.instance_ip = {
        dns_name : ip_address
    }
    execute(test_task, instance_ip=ip_address, option_arg=option_arg, hosts=[dns_name])

def update_noip(noip_user_pass, noip_user_email, noip_hostname):
    run('echo "export NOIP_USERPASSWORD=%s" >> .profile' % noip_user_pass)
    run('echo \'export NOIP_USERAGENT="curl/7.27.0 %s"\' >> .profile' % noip_user_email)
    run('echo "export NOIP_HOSTNAME=%s" >> .profile' % noip_hostname)
    run('echo "export NOIP_IP=%s" >> .profile' % env.instance_ip[env.host])
    put('deployables/registerNoIP.sh', 'registerNoIP.sh', mode=0755)
    run('./registerNoIP.sh')

    #run('curl --verbose --user %s --user-agent "curl/7.27.0 vijaypmreg+dns@gmail.com"'
    #        + ' https://dynupdate.no-ip.com/nic/update?hostname=myjeeves.no-ip.info&myip=%s' % (noip_user_arg, env.instance_ip[env.host]))
    #run('wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz')
    #run('mkdir noip-duc-linux')
    #run('tar xzvf noip-duc-linux.tar.gz -C noip-duc-linux --strip 1')
    #with cd('noip-duc-linux'):
    #    run('sudo make install')


def prepare_docker():
    run('sudo apt-get update')
    # run("echo 'Y' | sudo apt-get dist-upgrade")
    run("echo 'Y' | sudo apt-get install dtach")
    run("echo 'Y' | sudo apt-get install docker.io")
    run("sudo gpasswd -a %s docker" % env.user)
    run("sudo service docker.io restart")
    run("sudo ln -s /usr/bin/docker.io /usr/local/bin/docker")
    # need to logout and log back in for gpasswd to take effect 
    for env.host in connections.keys():
        connections[env.host].close()
        del connections[env.host]

def deploy_glasswebapp():
    run("docker pull vijaypm/glassenv")
    run("docker run -p 8080:8080 -p 22 -d vijaypm/glassenv")
    run("echo 'Y'")
    # with cd('jetty-distribution-9.1.5.v20140505'):
        # README - build helloglass.war from https://github.com/vijaypm/helloglass/helloglass
        # put('deployables/helloglass.war', 'webapps/helloglass.war')
        # README - download oauth.properties from your Google Developer console
        # put('deployables/oauth.properties', 'resources/oauth.properties')
        # run('dtach -c /tmp/mydtachsocket -z "java -jar start.jar"', pty=False)
        # run('dtach -A /tmp/mydtachsocket -z "java -jar ~/jetty-distribution-9.1.5.v20140505/start.jar"')
        # run('dtach -n `mktemp -u /tmp/mydtachsocket.XXXX` java -jar start.jar')



def deploy(noip_user_pass=os.getenv("NOIP_USERPASSWORD"), noip_user_email=os.getenv("NOIP_USERAGENT"), noip_hostname=os.getenv("NOIP_HOSTNAME")):
    if noip_user_pass is None or noip_user_email is None or noip_hostname is None :
        raise Exception('Provide a username:password, email and hostname for noip_user_arg, noip_user_email, noip_hostname')
    instance = LaunchEC2.launch_instance(cmd_shell=False)[0]
    sleeptime = 60
    print('sleeping for %d seconds' % sleeptime)
    time.sleep(sleeptime)

    env.instance_ip = {
        instance.public_dns_name:instance.ip_address
    }

    print('attempting to connect to %s' % instance.public_dns_name)
    execute(update_noip, noip_user_pass=noip_user_pass, noip_user_email=noip_user_email, noip_hostname= noip_hostname, hosts=[instance.public_dns_name])
    execute(prepare_docker, hosts=[instance.public_dns_name])
    execute(deploy_glasswebapp, hosts=[instance.public_dns_name])

def launchEC2():
    instance = LaunchEC2.launch_instance(cmd_shell=False)[0]
    print('launched instance %s' % instance.public_dns_name)



def undeploy():
    TerminateEC2.terminate_all()
    CleanEC2Security.clean_security_rules()

__author__ = 'vijay'

from fabric.api import env, local, run, execute, cd, put
import defaults
import os

env.user = defaults.EC2_USER_BITNAMI
env.key_filename = defaults.KEY_PATH
env.connection_attempts = 3

def deploy_glasswebapp():
    with cd('jetty-distribution-9.1.3.v20140225'):
        # run('dtach -A /tmp/mydtachsocket -z "java -jar ~/jetty-distribution-9.1.3.v20140225/start.jar"')
        run('dtach -n `mktemp -u /tmp/mydtachsocket.XXXX` java -jar start.jar')


def deploy():
    env.instance_ip = {
        'ec2-54-211-154-88.compute-1.amazonaws.com':'54.211.154.88'
    }

    print('attempting to connect to %s' % env.instance_ip)
    execute(deploy_glasswebapp, hosts=[env.instance_ip.keys()[0]])

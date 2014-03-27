__author__ = 'vijay'

### Approach 1
#def foo():
#    with settings(host_string='apycat'):
#        run(...)

### Approach 2
#def bar():
#    run(...)
#
#def foo():
#    execute(bar, hosts=['apycat'])

### Approach 3
#from fabric.api import env, run
#
#def set_hosts():
#    env.hosts = ['host1', 'host2']
#
#def mytask():
#    run('ls /var/www')
#
#vijay@vijay-laptop:~/PycharmProjects/MyFirstAWS$ fab set_hosts mytask

from fabric.api import env, run, execute

class FabricSupport:
    def __init__(self):
        pass

    def hostname(self):
        run("hostname")

    def df(self):
        run("df -h")

    def execute(self,task,hosts):
        get_task = "task = self.%s" % task
        exec get_task
        execute(task,hosts=hosts)

hosts = ['localhost']

myfab = FabricSupport()
myfab.execute("df",hosts) # fails with ImportError: cannot import name Random
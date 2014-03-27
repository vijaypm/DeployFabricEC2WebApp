__author__ = 'vijay'

import boto
import boto.ec2
import defaults

boto.set_stream_logger("boto")

def clean_security_rules(ec2_region=defaults.EC2_REGION, group_name='myucsc'):
    # Create a connection to EC2 service.
    # You can pass credentials in to the connect_ec2 method explicitly
    # or you can use the default credentials in your ~/.boto config file
    # as we are doing here.
    #ec2 = boto.connect_ec2()
    ec2 = boto.ec2.connect_to_region(ec2_region)

    group = ec2.get_all_security_groups(groupnames=[group_name])[0]

    print "Revoking "
    print vars(group)

    for rule in group.rules:
        print vars(rule)
        print 'Rule protocol %s' % rule.ip_protocol
        print 'Rule from port %s' % rule.from_port
        print 'Rule to port %s' % rule.to_port
        print 'Rule cidr %s' % rule.grants[0]
        group.revoke(ip_protocol=rule.ip_protocol,
                     from_port=rule.from_port,
                     to_port=rule.to_port,
                     cidr_ip=rule.grants[0])

    #group = ec2.get_all_security_groups(groupnames=['myucsc'])[0]

    #print 'Security rules %s' % group.rules



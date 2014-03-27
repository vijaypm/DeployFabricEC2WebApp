__author__ = 'vijay'
import boto.ec2
import defaults

def stop_all(ec2_region=defaults.EC2_REGION):
    ec2_conn = boto.ec2.connect_to_region(ec2_region)
    reservations = ec2_conn.get_all_instances(filters = {"instance-state-name":"running"})
    reservations
    instances = [i for r in reservations for i in r.instances]
    instances
    ec2_conn.stop_instances([i.id for i in instances])
    return

def terminate_all(ec2_region=defaults.EC2_REGION):
    ec2_conn = boto.ec2.connect_to_region(ec2_region)
    reservations = ec2_conn.get_all_instances()
    reservations
    instances = [i for r in reservations for i in r.instances]
    instances
    ec2_conn.terminate_instances([i.id for i in instances])
    return
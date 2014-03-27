__author__ = 'vijay'
import boto
boto.set_stream_logger("boto")

s3 = boto.connect_s3()
rs = s3.get_all_buckets()
print 'S3 buckets'
for b in rs:
    print b

print 'S3 regions'
import boto.s3
regions = boto.s3.regions()
for r in regions:
    print r
s3_conn = boto.s3.connect_to_region('us-west-1', debug=2)

print 'EC2 regions'
import boto.ec2
regions = boto.ec2.regions()
for r in regions:
    print r

#ec2_conn = regions[0].connect()
ec2_conn = boto.ec2.connect_to_region('us-west-1', debug=2)
reservations = ec2_conn.get_all_instances()
reservations
#[Reservation:r-615f6302, Reservation:r-26d09a44, Reservation:r-b3e903d5]
#instances = []
#for r in reservations:
#    instances.extend(r.instances)
instances = [i for r in reservations for i in r.instances]
instances
ec2_conn.stop_instances([i.id for i in instances])
ec2_conn.terminate_instances([i.id for i in instances])
#ec2_conn.terminate_instances([reservation.instances[0].id for reservation in ec2.get_all_instances()])


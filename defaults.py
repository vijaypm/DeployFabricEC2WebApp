__author__ = 'vijay'
import os
import boto

#EC2_REGION='us-east-1'
EC2_REGION='us-west-1'


AMI_UBUNTU14_64WEST='ami-79b4b73c'

AMI_BITNAMI_DJANGOSTACK_UBUNTU32 = 'ami-1dd99174' # us-east-1 region
AMI_UBUNTU12_32='ami-59b4a930' #12.04
#AMI_UBUNTU14_64='ami-864d84ee' #hvm - Non-Windows instances with a virtualization type of 'hvm' are currently not supported for this instance type.
AMI_UBUNTU14_64='ami-384d8450' #paravirtual
#AMI_UBUNTU32='ami-6f071b06' #12.10
#AMI_BITNAMI_DJANGOSTACK_UBUNTU32 = 'ami-cee8dd8b' # us-west-1 region
EC2_AMI = AMI_UBUNTU14_64WEST

EC2_USER_BITNAMI='bitnami'
EC2_USER_UBUNTU='ubuntu'
EC2_USER=EC2_USER_UBUNTU

MICRO_INSTANCE = 't1.micro'

INSTANCE_TAG=EC2_REGION

KEY_NAME=EC2_REGION
KEY_EXTENSION='.pem'
KEY_DIR='~/.ssh'
KEY_PATH = os.path.join(os.path.expanduser(KEY_DIR),
                                KEY_NAME+KEY_EXTENSION)
WEB_PORT=8080
CIDR='0.0.0.0/0'
#boto.set_stream_logger("boto")



'''
ap-northeast-1 Asia Pacific (Tokyo) Region

ap-southeast-1 Asia Pacific (Singapore) Region

ap-southeast-2 Asia Pacific (Sydney) Region

eu-west-1 EU (Ireland) Region

sa-east-1 South America (Sao Paulo) Region

us-east-1 US East (Northern Virginia) Region

us-west-1 US West (Northern California) Region

us-west-2 US West (Oregon) Region
'''
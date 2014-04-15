__author__ = 'vijay'
import os
import boto

EC2_REGION='us-east-1'
#EC2_REGION='us-west-1'
AMI_BITNAMI_DJANGOSTACK_UBUNTU32 = 'ami-1dd99174' # us-east-1 region
AMI_UBUNTU32='ami-59b4a930' #12.04
#AMI_UBUNTU32='ami-6f071b06' #12.10
EC2_AMI = AMI_UBUNTU32
#AMI_BITNAMI_DJANGOSTACK_UBUNTU32 = 'ami-cee8dd8b' # us-west-1 region
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
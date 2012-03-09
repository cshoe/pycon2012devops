from fabric.api import *
from fabric.decorators import task, roles
from chef.fabric import chef_roledefs

### set me. full path to where your AWS key file is located. ###
env.key_filename = ''
env.user = 'ubuntu'

env.roledefs = chef_roledefs(hostname_attr='ec2.public_hostname')

@task
@roles('base')
def chef_client():
    sudo('chef-client')
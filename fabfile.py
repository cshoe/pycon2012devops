from fabric.api import *
from fabric.decorators import task, roles
from chef.fabric import chef_roledefs

def use_ec2_hostname(node):
    if node.attributes.has_dotted('fqdn'):
      return 'fqdn'
    else:
      return 'ec2.public_hostname'

env.roledefs = chef_roledefs(hostname_attr = use_ec2_hostname)

@task
@roles('base')
def chef_client():
    sudo('chef-client')
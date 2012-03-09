Working "solutions" for Lab 2 and Lab 3 from the DevOps for Python: Doing More With Less at PyCon 2012.

Props to coderanger for a great tutorial.

**NOTICE**

I removed the .chef dir due to these files being specific to your environment. You should use the knife.rb and *.pem
file that came with your version of Noah's zip.

Lab 2
-----

In *cookbooks/apache2/recipes/default.rb* is a super simple recipe
to get apache installed and running with a conf file at
*/etc/apache2/sites-enabled/site.conf*.

The only other tweak to the original code is the addition of the
cookbook to the base role's run list.

::

    run_list "recipe[git]", "recipe[build-essential]", "recipe[apache2]"

After we do this, the role needs to be updated.

::

    knife role from file base.rb

Now if you run

::

    knife role show base

you should see something like:

::

        chef_type:            role
    default_attributes:
    description:          Simple base setup
    env_run_lists:
    json_class:           Chef::Role
    name:                 base
    override_attributes:
    run_list:             recipe[git], recipe[build-essential], recipe[apache2]

Notice the addition of *recipe[apache2]*.

**Upload the cookbook.**

::

    knife cookbook upload apache2

**Launch an instance with the same command you did in Lab 1**

::

    knife ec2 server create -x ubuntu -r 'role[base]'

If you go to the IP that is outputted by the chef-client run, you should see a familiar apache *It works!* page.


Lab 3
-----

**Install Requirements**

#. Create and activate a virtualenv using your preferred method.
#. Use pip to install requirements.

::

    cd <project_root>
    pip install reqs.txt

One small caveat... if you open reqs.txt, you'll notice that it's pointing to a fork of pychef. The version on PyPI doesn't yet support the *hostname_attr* kwarg which is necessary to get the public IP for your box. I originally installed the current version from coderanger's repo but there were a couple small errors.

**Add the Path to Your SSH Key to fabfile.py**

::

    env.key_filename = '/path/to/your/key.pem'

Run chef-client on your box with Fabric:

::

    fab chef_client

You should see the output from the Chef run in your terminal.

Don't Forget
------------

Kill your boxes with the web interface or *knife* when you're done. They cost money.
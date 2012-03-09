Working "solutions" for Lab 2 and Lab 3 from the DevOps for Python: Doing More With Less at PyCon 2012.

Props to @coderanger for a great tutorial.

**NOTICE**

I removed the .chef dir due to these files being specific to your environment. You should use the knife.rb and *.pem
file that came with your version of Noah's zip.

Lab 2
-----

In *cookbooks/apache2/recipes/default.rb* is a super simple recipe
to get apache installed and running with a conf file at
*/etc/apache2/sites-enabled/site.conf*.

The only other tweak to the original code is the addition of the
cookbook to the base role's runlist.

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
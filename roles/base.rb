
name "base"
description "Simple base setup"
run_list "recipe[git]", "recipe[build-essential]", "recipe[apache2]"

package "apache2" do
    action :install
end

service "apache2" do
    action :enable
end

template "/etc/apache2/sites-enabled/site.conf" do
    action :create
    source "site.erb"
    owner "www-data"
    group "users"
    mode "644"
end

service "apache2" do
  action :start
end

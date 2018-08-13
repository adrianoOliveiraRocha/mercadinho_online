# mercadinho_online


Config django project with apache2
conf: sudo gedit /etc/apache2/sites-available/000-default.conf

logs: sudo gedit /var/log/apache2/error.log

Install Packages from the Ubuntu Repositories:
sudo apt-get update
sudo apt-get install python-pip apache2 libapache2-mod-wsgi
sudo apt-get update
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3

Configure a Python Virtual Environment:
sudo pip3 install virtualenv

Put the virtualenv and a project within /var/www because there you will haven't
problems with permissions  

Configure /etc/apache2/sites-available/000-default.conf

<VirtualHost *:80>
	<Directory /var/www/html>
                Options Indexes FollowSymLinks MultiViews
                AllowOverride All
                Order allow,deny
                allow from all
	</Directory>

	<Directory /var/www/html/>
        AllowOverride All
    </Directory>
    
	# The ServerName directive sets the request scheme, hostname and port that
	# the server uses to identify itself. This is used when creating
	# redirection URLs. In the context of virtual hosts, the ServerName
	# specifies what hostname must appear in the request's Host: header to
	# match this virtual host. For the default virtual host (this file) this
	# value is not decisive as it is used as a last resort host regardless.
	# However, you must set it for any further virtual host explicitly.
	ServerName localhost

	ServerAdmin webmaster@localhost
	DocumentRoot /var/www/html

	# Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
	# error, crit, alert, emerg.
	# It is also possible to configure the loglevel for particular
	# modules, e.g.
	#LogLevel info ssl:warn

	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

	# For most configuration files from conf-available/, which are
	# enabled or disabled at a global level, it is possible to
	# include a line for only one particular virtual host. For example the
	# following line enables the CGI configuration for this host only
	# after it has been globally disabled with "a2disconf".
	#Include conf-available/serve-cgi-bin.conf

	Alias /static /var/www/html/djangoapache/static
	<Directory /var/www/html/djangoapache/static>
	  Require all granted
	</Directory>

	<Directory /var/www/html/djangoapache/djangoapache>
	  <Files wsgi.py>
	    Require all granted
	  </Files>
	</Directory>

	WSGIDaemonProcess djangoapache python-home=/var/www/html/Python/djangoapache python-path=/var/www/html/djangoapache
	WSGIProcessGroup djangoapache
	WSGIScriptAlias / /var/www/html/djangoapache/djangoapache/wsgi.py

</VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet

In this case, this app is in port 80



# you need this command:
# sudo apt install apache2-dev



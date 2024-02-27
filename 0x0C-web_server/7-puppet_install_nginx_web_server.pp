# script to install nginx web server using puppet

exec { 'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get install -y nginx ; echo "Hello World!" | sudo tee /var/www/html/index.html ;
	       sudo sed -i "s/server_name _;/server_name _ ;\n\trewrite ^\/redirect_me https:\/\/github.com\/ASLawan permanent;/" 
	       /etc/nginx/sites-available/default ; sudo service nginx start',
}


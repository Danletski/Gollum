# Gollum

Instuctions:
#Pull the folder

  Run "vagrant up" inside the project folder (Where the Vagrant file is found).
#The Vagrant folder should be mounted inside the Vagrant host to /etc/ansible.
#SSh to the vagrant host:
  "vagrant ssh"
#cd to "/etc/ansible" 
#nginx_php - included the Docker file for the nginx docker machine + nginx.conf file
#php_app includes the Docer file for the 2 web app servers
  run "sudo docker-compose up -d" 
#It should create 2 web app servers, and 1 nginx LB.
#Run the test Script testall.py
The script will return if the proxy + the 2 web servers reply or not.

Jenkins Pipeline File available in the folder.

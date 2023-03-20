# Create a new volume name my_volume.
1- sudo docker volume create my_volume

2- sudo docker volume ls
DRIVER    VOLUME NAME
local     my_volume

# Create a new docker container using "nginx" image and mount "my_volume" to the container's "usr/share/nginx/html" directory. 
1- sudo docker run --name ng
                   -p 8080:80 
                   -v my_volume:/usr/share/nginx/html 
                   -d nginx:latest

2- sudo docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                   NAMES
350008ae050f   nginx:latest   "/docker-entrypoint.…"   20 minutes ago   Up 20 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   ng

# Verify the nigix continer.
1- get to the browser 

2- http://localhost:8080

# Create a file "index.html".
<!DOCTYPE html>
<html>
<head>
	<title>My Website</title>
</head>
<body>
	<h1>Welcome to my Website!</h1>
	<p>This is a test page.</p>
</body>
</html>

# Using docker cp copy "index.html" from the source path to the my_volume".
1- sudo docker cp index.html  
               350008ae050f:/usr/share/nginx/html
2- sudo docker exec -it 350008ae050f /bin/bash

3- root@350008ae050f:/# ls
bin   docker-entrypoint.d   home   media  proc	sbin  tmp
boot  docker-entrypoint.sh  lib    mnt	  root	srv   usr
dev   etc		    lib64  opt	  run	sys   var

4- root@350008ae050f:/# cd usr

5- root@350008ae050f:/usr# ls
bin  games  include  lib  libexec  local  sbin	share  src

6- root@350008ae050f:/usr# cd share/

7- root@350008ae050f:/usr/share# ls
X11		 debianutils  info	  misc		  tabset
adduser		 dict	      java	  nginx		  terminfo
base-files	 doc	      keyrings	  pam		  ucf
base-passwd	 doc-base     libc-bin	  pam-configs	  xml
bash-completion  dpkg	      lintian	  perl5		  zoneinfo
bug		 fontconfig   locale	  pixmaps	  zsh
ca-certificates  fonts	      man	  polkit-1
common-licenses  gcc	      maven-repo  readline
debconf		 gdb	      menu	  sensible-utils

8- root@350008ae050f:/usr/share# cd nginx/

9- root@350008ae050f:/usr/share/nginx# ls
html

10- root@350008ae050f:/usr/share/nginx# cd html/

11- root@350008ae050f:/usr/share/nginx/html# ls
50x.html  index.html

12- root@350008ae050f:/usr/share/nginx/html# cat index.html 
<!DOCTYPE html>
<html>
<head>
	<title>My Website</title>
</head>
<body>
	<h1>Welcome to my Website!</h1>
	<p>This is a test page.</p>
</body>
</html>

# Verify the inde.html.
1- get to the browser

2- http://localhost:8080

# stop and remove the container. 
1- sudo docker stop 350008ae050f
350008ae050f

2- sudo docker rm 350008ae050f
350008ae050f

# Create a new docker container using "httpd" image and mount the "my_volume" to the container's "/usr/local/apache2/htdocs" directory.
1- sudo docker run --name httpda3 
                   -p 8081:80 
                   -v my_volume:/usr/local/apache2/htdocs 
                   -d httpd
76d1edf5d093d06950b541f4dbc02e1a0a3bfeb4e95816962e8ba4a0b75156c9

2- sudo docker ps
CONTAINER ID   IMAGE     COMMAND              CREATED         STATUS         PORTS                                   NAMES
76d1edf5d093   httpd     "httpd-foreground"   5 seconds ago   Up 4 seconds   0.0.0.0:8081->80/tcp, :::8081->80/tcp   httpda3

3- sudo docker inspect 76d1edf5d093
"Ports": {
                "80/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "8081"
                    },
                    {
                        "HostIp": "::",
                        "HostPort": "8081"
                    }
                ]

# verify the httpd.
1- go to browser

2- http://localhost:8081 

# create a new file "about.html" on your host machine and add some text to it.
1- nano about.html
<!DOCTYPE html>
<head>
	<title>My About Page</title>
</head>
 <div class="about-section">
  <h1>This is my about Us Page</h1>
  <p>I am a freshie.</p>
  <p>A meticulous and organized individual seeking an entry level job in the field of Devops. Proficient in Ubuntu(linux) & MYSQL(workbench).</p>
 </div>

<h2 style="text-align:center">My Contact Info</h2>
<div class="row">
  <div class="column">
    <div class="card">
      <div class="container">
        <h2>Syed Musa Ali</h2>
        <p class="title">Devops Engineer (INSHALLAH)</p>
        <p>Thankyou for reviewing my about page. </p>
        <p>syedmusaali359@gmail.com</p>
	<p>+92-3314666427</p>
        <p><button class="button">Contact</button></p>
      </div>
    </div>
  </div>

# Copy "about.html" on your host to "my_volume" to the container's "/usr/local/apache2/htdocs" directory.
1- sudo docker cp about.html  5b6164bde3f5:/usr/local/apache2/htdocs

2- udo docker exec -it 5b6164bde3f5 /bin/bash

3- root@5b6164bde3f5:/usr/local/apache2# ls
bin  build  cgi-bin  conf  error  htdocs  icons  include  logs	modules

4- root@5b6164bde3f5:/usr/local/apache2# cd htdocs/

5- root@5b6164bde3f5:/usr/local/apache2/htdocs# ls
50x.html  about.html

# verify that the file is accessible on browser
1- http://localhost:8081/about.html
yes its accessible.

# Stop and remove the container
1- sudo docker stop 5b6164bde3f5

2- sudo docker rm 5b6164bde3f5

# remove the "my_volume" volume.
1- sudo docker volume rm my_volume
my_volume

2- udo docker volume ls
DRIVER    VOLUME NAME

# push the codebase to the github


# Fusemachines_project
<h1>Steps:

download the repo from github from https://github.com/NischalBhandari/Fusemachines_project.git

If you do not have docker or docker-compose please check out resources in the internet.

Here are some links 

https://docs.docker.com/compose/install/

https://docs.docker.com/engine/install/ubuntu/



then type the following commands

note: please download a version of docker-compose such that  >= 1.27.0

*First also setup your user permissions for docker*

*if docker group doesnot exist then* 

*sudo groupadd docker*

*sudo usermod -aG docker ${USER}*

*Then logout or restart the system*

If you get any errors in docker-compose build and docker-compose up use 

*sudo docker-compose build and sudo docker-compose up  (this is not a good solution/some permission issues in docker-compose.yml )* 



 **docker-compose build**

**docker-compose up**



<h2> Setup your database</h2> 

The above commands will run two docker containers one with mongodb and one with the python application 

**Then use the following command** 
**docker ps** 

This command will give you the output of running containers in the system with the $CONTAINER_ID

**docker exec -it $CONTAINER_ID bash **

*For e.g: docker exec -it 0bc153158b8e bash*

Then choose the CONTAINER_ID with the IMAGE mongo:4.0.8
then implement the following command

then inside the database use the command 

**mongo -u mongodbuser -p**

This will prompt you for the password
After entering the password you created  in the file docker-compose.yml (default is fiberoptics12)
you can now access the database commandline

**Inside the Database commandline place following commands**

**use flaskdb**



**db.createUser({user: 'flaskuser', pwd: 'fiberoptics12', roles: [{role: 'readWrite', db: 'flaskdb'}]})**



**exit**

now your database is ready 

<h2>Running the program

Now as your database and application is ready. It should be running two containers you can check it with docker ps command

after this you have to access the ip address of the host machine running the docker container with port 5000

For eg: http://192.168.1.110:5000



<h2>The Application</h2>

The application is a simple todo app that can add list of things todo in a day.

It also has the functionality of deleting the task and delete all the tasks at once.

The app is very simple but serves its purpose of showing the use of docker containers



<h2>Jenkinsfile</h2>



The jenkinsfile is a file that describes how we can build this application using jenkins 

For using the jenkinsfile till now only the dockerconainer is added till now 


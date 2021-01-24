# Fusemachines_project
<h1> To Create a user for your Database</h1>
download the repo from github from https://github.com/NischalBhandari/Fusemachines_project.git
then run the docker-compose build
then run docker-compose up 

This will run two containers one with mongodb and one with the python application 
Then use the following command 
docker ps 
This command will give you the output of running containers in the system
Then choose the container with the tag mongo
then implement the following command
docker exec -it $TAG_NAME bash
then inside the database use the command 
mongo -u nischal -p
This will prompt you for the password
After entering the password you create in the file (default is fiberoptics12)
you can now access the database

**Use the following commands**
use flaskdb
db.createUser({user: 'flaskuser', pwd: 'fiberoptics12', roles: [{role: 'readWrite', db: 'flaskdb'}]})
exit


now your database is ready 

#Project title
Item Catalog Application

#Overview
The RESTful web applicaion provides a list of items within a variety of categories, using Python Framework Flask along with implementing third-party Oauth authentication, as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

#Prerequisites
1) install python 3.6
   --you can install the python packages required through the commands:
	1-"pip freeze > requirements.txt" =>to create one run
	2-"pip install -r requirements.txt" =>install packages
2) install git bash
3) install virtual machine
4) install vagrant
5) install Flask module for python
6) install Udacity Vagrant file 

#Running
To test the project:
1) open git bash
2) cd into the directory 'fsnd-virtual-machine'
3) cd into vagrant directory
3) Put the directory "CatalogItem" into the vagrant directory
4) type "vagrant up" command-line in git bash
5) type "vagrant ssh" command-line
6) cd into CatalogItem directory
7) run the command "python Database_setup.py" to create the database and create the tables
8) run the command "python categoriesdb.py" to fill the data into the database
7) run the command "python project.py"
8) once the server is running you can open the browser and type "localhost:5000" to view       home page
9) after finishing type "CTRL + c" to close the server
# BasicFastAPI

BasicFastAPI backend

A backend implementation of FastAPI portal that allow to create users, groups and managing session to be used in simulations or game based applications.

In this github we document the installation  from setting github, visual studio and everything needed to create a python app with the following functions and features:

Environment
	Language: Python 3.12
	Database MongoDB hosted at https://cloud.mongodb.com/ 
	Hosting: railway.app at https://basicfastapi-production.up.railway.app/docs 
	Connected to Google to use oAuth2 in the future settings
	Using Visual Studio Code as a development environment 
	
Users are registered using a email, there is email validation for user creation, support to recovery password using email.

The steps to build the app are:

- Create a Github 
- Create a virtual environment in Python
- Install FastAPI
- Set the connection with MongoDB
	- Database: BasicFastAPI
	- Collections: Users
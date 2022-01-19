 I have designed a basic inventory web application using Django which is one of Python’s leading frameworks for web development. I decided to use Django because it encourages rapid and clean web applications.

PREREQUISITES
> For you to follow the steps below, you need to have the following packages installed:
-	Python (Version 2.7 or higher)
-	Django
-	Virtualenv

STEPS
1.	Create a Virtual Environment: To create a virtual environment, just run the following command on the command prompt
```
    virtaulenv [custom_name_of_your_virtual_environment]
```

2.	Create a requirements.txt file: If you’re on a mac or a git bash terminal, Simply run
 ```
    pip freeze > requirements.txt
```
This will automatically create a requirements.txt and paste the contents of the pip freeze command into the requirements file.  If you’re on a windows machine, manually create a requirements.txt  file, simply run 
```
    pip freeze 
``` 
on your command prompt then copy and paste the output of the command into the file.

3.	Install all dependencies present in the projects’ requirements.txt file: To do this, run 
``` 
    pip install -r requirements.txt
```
in your terminal.

4.	Activate the virtual environment you have created for this project: To activate a virtual environment, choose the method that suits your machine.

•	Windows:
 ```
    [virtual_env_name]\scripts\activate
```
•	Linux: 
``` 
    source ./[virtual_env_name]/scripts/activate
```
5.	Change into the project’s directory from your command prompt, terminal or git bash window: In order to run the next command, you have to ensure that you’re in the correct path for your project. e.g if the path is 
``` 
C:\Users\hp\Downloads\django_master\django_project
```
One would change into it this way:
```
    C:\Users\hp
```
``` 
    cd downloads
```
```
    cd django_master
```
```
    cd django_project
```
6.	Run the server: To run the server, input the following command into the terminal
```
 python manag.py runserver
 ```
7.	Copy and paste the Url generated into a suitable browser. The url is somthing similar to this:
```
C:\Users\hp\Pictures\MAIN\project\users\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 18, 2022 - 20:13:45
Django version 4.0.1, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
8.	Register via the link in the far right of the home Page 

9.	Login with your credentials
10.	Now, Explore all the functionalities.




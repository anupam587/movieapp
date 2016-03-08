This is a Movie Database application which is built using python Django framework following pep8 conventions.  

This contains two user ends  

first one is for visitors of the app they can access it on http://127.0.0.1:8000/  
which contains a nice UI/UX built using bootstrap,  
Displays upcoming/top-rated/latest movie releases as well as  
movies according to their movie genres.  

Second is for administratin pupose for staff members ,they can access it on http://127.0.0.1:8000/admin  
they can control what should be displayed on vistors page  
After login to admin panel under movies section four section are listed.  
Actors(casts) / Directors/ Categorys/ Movies  
You can go to each section and add data for different sections.  

Significant features for devlopers:     
1. A movie can contain multiple Actor and Actor can be assigned to muliplte movies (ManyToMany relation b/w Actor and Movie)  
2. A movie can contain single Director but director can do multiple movies(ManyToOne relation b/w Director and Movie)    
3. A movie can follow up inside many type of movie genres (Romance/Drama/Comedy etc.) (ManyTOMany relation b/w Movie and Category)  


Follow the Below Instruction to install this app.  
1. Python and Django framework must be installed in your system  
2. Download and extract the project .  
3. Go to the project-dir (cd movieapp)  
4. execute 'source bin/activate'  
5. Go to the moviedb folder (cd moviedb)  
6. execute 'python manage.py createsuperuser' to create a admin profile , above execution prompt to ask username , email, password to crete a admin user-profile.  
7. execute 'python manage.py makemigrations' to do all database related migrations  
8. execute 'python manage.py migrate' to apply the above migrations  
9. execute 'python manage.py collectstatic' to collect static files to appropraite locations  
10. Finally you can start the server using 'python manage.py runserver'  
11. this will provide a URl : http://127.0.0.1:8000/,  so now go to this url and enjoy :)  
12. Go to http://127.0.0.1:8000/admin/ , here he will prompt for username and password that is same as you created during admin profie setup as described in step 6  
13.In case if the port 8000 is used by some another application, so execute 'python manage.py runserver port_no' here give some other port no which is not used by any other application  
Eg: python manage.py runserver 8899  
now go to the vistor section using http://127.0.0.1:8899/  
and access admin section using http://127.0.0.1:8000/admin/  

# LMD
 django based api project integrated with jwt authentication
 
 Project setup
 activate the virtual environment by venv/scripts/activate.
 Install all the dependencies using pip-  install pip3 install -r requirements.txt
 connect Mysql database by creating a database- librarydb
 make migrations with the command- py manage.py makemigrations
 run these migrations= py manage.py migrate
 then runserver with- py manage.py runserver
 
 API Guide
 POSTMAN collection-https://www.postman.com/dark-zodiac-789458/workspace/library-management-system/collection/19572418-ade6541d-ced3-489e-b03e-e27617ee9425?action=share&creator=19572418
 step 1 - register a user with the api point REGISTER
 step2 - login the user with api point LOGIN
 step3 - copy the access token for authentication to other api's
 
 API Explanation
 1-create book - a book can only be created by user_type = FACULTY and will raise an error if a STUDENT tries to create it.
 2 - individual book - an individual book can be seen by both the user_types.
 2- all books - all books can be seen by all user_types
 3- delete book - pass in the id of the book in parameters to delete the book. a book can only be deleted by the FACULTY member.
 4- update book - pass in the id of the book in parameters to update the book. a book can only be deleted by the faculty member.
 5-create member - a member can be only created by FACULTY member. (books,user) are mandatory to create and assign a member to a book. a book will be assigned upon creation.
 6- all members GET - all members can be viewed by both FACULTY and STUDENT user-type.
 
 7- update members UPDATE - a book can be returned by a student by not returning anything in (request.data). a book can be borrowed by returning the book id in the data and if a user already has a book issued and returns the first book at the sametime, new book will be issued and its status will change to BORROWED and the former books status will change to AVAILABLE. If a book is already BORROWED an error will be raised at the same time.
 
 8-get individual member - a member can be viewed by both FACULTY and STUDENT.
 

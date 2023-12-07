# Library-management-system
Library management system in django

Endpoints

You can run the project and see the swagger schema for request and response required for each api.

Also,

Get/api/book requires no authentication

But to run Post/api/add and Put/api/update you will have to first login

for login use the Post/api/login endpoint and use the following username and password details

Username='admin'
Password='AnmolShriv'

for authentication purpose this api will return a jwt token, which you will have to use in add and update api.

for database connections define your database name, user, host and password in the .env file

I have also provided a sql file that you can initially run after migration, so that dummy data gets populated 



# userapi
Attainia user-activity-code-challenge backend

Create a Django Rest Framework application that has an endpoint that can produce the content of the users.json file. 
Your application should be able to return all users, users that have not logged in, and users that have logged in.

Ideas:
https://github.com/Lmcmaaser/movieapi
create tables (users, loggedIn, noLogin) in DRF
create python script that prompts for filename (users.json)
  parse file
  inserts or ignores data to database

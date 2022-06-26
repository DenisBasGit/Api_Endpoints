# Api_Endpoints

# STEP 1
  git clone https://github.com/LazyCORE/Api_Endpoints
  
# STEP 2
  Connect to local database:
  
  1.You need create mysql database with name 'wow'
  2.In .env-file change params: DATABASE.USER, DATABASE.PASSWORD
  
# STEP 3 
    RUN:
  1.Enter: cd Api_Endpoints.
  
  2.Enter: python3 manage.py makemigrations
  
  3.Enter: python3 manage.py migrate
  
  You need to create superuser for checking admin panel
  
  1. python3 manage.py createsuperuser
 
# API ENDPOINTS
1. http://127.0.0.1:8000/api/v1/directions (Get a list of directions)
3. http://127.0.0.1:8000/api/v1/doctorlist/ (Get a list of Doctors, you can see pagination)
  2.1 http://127.0.0.1:8000/api/v1/doctorlist/?ordering=direction (filtering by direction )
  2.2 http://127.0.0.1:8000/api/v1/doctorlist/?minyears_of_experience=2&ordering=years_of_experience (filtering by experience)
4. http://127.0.0.1:8000/api/v1/doctorlist/sort (by default sorted by number sort and name)
  3.1 http://127.0.0.1:8000/api/v1/doctorlist/?ordering=date (sorted by date)
  3.2 http://127.0.0.1:8000/api/v1/doctorlist/?ordering=years_of_experience (sorted by experience )

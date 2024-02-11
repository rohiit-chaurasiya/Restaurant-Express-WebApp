# Restaurant-Express-WebApp

##### Live Here- http://restaurantexpress.pythonanywhere.com/

### Welcome to Let's! This web application allows users to explore restaurant menus, select items, and place orders.

# Features
 - Users can explore various restaurant menus.
 - They can select items from the menus.
 - Users can add selected items to their Cart system.
 - The Cart system allows users to review and modify their selected items before finalizing their orders.
 - Once satisfied with their selection, users can proceed to place their orders.
 - Developed an admin page accessible only to administrators.
 - Administrators have full control (CRUD) over menu items and orders.
 - Admins can add new menu items, update existing items, or remove items that are no longer available.
 -  Integrated with the Razorpay Payment Gateway for processing payments securely.




## Follow the steps below to set up and install the project dependencies:

Clone this repository:
```
git clone https://github.com/RohitAayushmaan/HomeDeliveryRestaurants.git
```

Access:
```
cd Restaurant-Express-WebApp
```

Install virtualenv:
```
pip install virtualenvwrapper
```

Creating the virtualenv:
```
mkvirtualenv venv_name
```

After creating virtial environment we need to activate it:
```
workon venv_name
```

Package you need to install:
```
pip install -r requirement.txt
```

Create all the tables in database.
```
python manage.py migrate
```

## Run the project
```
python manage.py runserver
```

The server will initialize in the http://localhost:8000


# HomeDeliveryRestaurants

### Live Here- http://restaurantexpress.pythonanywhere.com/
![hm1](https://github.com/RohitAayushmaan/HomeDeliveryRestaurants/assets/52812829/789a30cd-e618-454f-baa7-ec8fc6c74611)

"HomeDeliveryRestaurants" is a web-based food ordering application developed using the Django framework. 

For users, developed an intuitive interface to explore various restaurant menus, select items, and place orders. It also provide a Cart system that enables users to make a list of selected food items before finalizing their orders. Once the selection is complete, users can proceed to place their orders.

On the administrative side, developed an admin page that grants administrators full control over the menu items and orders. The admin page facilitates CRUD (Create, Read, Update, Delete) operations on the menu items. Admins can easily make changes to the menu by adding new items, updating existing ones, or removing items that are no longer available. Additionally, they can monitor and manage the orders placed by users.

This application also integrates with the Razorpay online payment gateway. This integration enables users to make secure online payments for their orders.

## To run this project, follow these necessary steps:

Git Clone this repo - 
```sh
git clone https://github.com/RohitAayushmaan/HomeDeliveryRestaurants.git
```
Navigate into the cloned project directory using cd <HomeDeliveryRestaurants>


Make Virtual Environment and install Django
```sh
pip install virtualenvwrapper-win
mkvirtualenv envName
workon envName
pip install django
```

# Create Database
```sh
python manage.py migrate
python manage.py makemigrations
```

# Now Run 
```sh
python manage.py runserver
```



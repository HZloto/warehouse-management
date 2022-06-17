# warehouse-management
<b>This Python script helps manage stock inventory for a woodworking company. It supports adding, removing, displaying and saving locally a report on stocks available in a warehouse.
Functionalities</b>

<h1>How to use</h1>

Make sure that Stock.py, Warehouse.py and main.py are in the same folder in you local OS. 
Open your terminal to the location of the folder and type “python main.py”
A menu will appear. Use the keypad to navigate (e.g. to add stock, input “1” in the Input Request box.
When done, hit “5” on the main menu to exit the script. (NOTE: All inventory will be reset to 0 after exiting the app). 

<h1>Design and architecture</h1>

This app is developed with using Python with an “Object Oriented Programming” focus. It is split between three scripts described more in depth below. In short, all the constraints and information storing is in the Stock.py script, and all the display and app components are in Warehouse.py.

<h2>Stock.py</h2>

This script stores a class called “Generic Stock”, which defines a generic stock type and methods to add and remove stock. All stock have the “quantity” attribute, which is used as the memory endpoint to store the inventory every time an operation is done, to avoid using a .csv file. 

We use class inheritance to define three types of stock: Redwood, Maple and Oak. 
The super function allows to keep the methods of the Generic Stock function. 

Each inherited class has a particular attribute that is unique to each type of stock: Redwood has density, Maple has humidity, and Oak has varnish. 

We use a separate script for stock to keep all the definitions of functions and attribute in a tidy space without all the visual components of the app.

<h2>Warehouse.py</h2>

The Warehouse script contains the MainWarehouse class which includes all the functionalities of the app and its visual aspects. 

It has: 

<li>An init function: we use it to create objects for our stock and define a unit price, init quantity
<li>add_stock: provides an interface to pick stock type to add, and what quanitity.
<li>remove_stock: provides an interface to pick stock type to remove, and what quanitity
<li>get_stock: Lets the user get a report on an individual stock
<li>display_inventory: gives the user a full report of the inventory with the option to save the report as a .txt file
<li>exit_program: Calls python’s exit function
<li>input_check: Verifies that all menu inputs are integers
<li>display_menu: Prints the different choices presented to the user and execute the function of the chosen path.

  <b>Note:</b> to avoid unwanted app termination, all the input checks are made using try/except or if statement. Assert statements can be found in the test script (see below.)

<h2>Main.py</h2>

Imports the elements of the MainWarehouse class from the Warehouse script. 
Triggers the display_menu() function as an entry point to access the app. 


<h1>Testing</h1>

A test.py script is provided in the GitHub files. It features an edited version of the app to test its functionalities. All the user inputs are replaced by hard-coded answers to run through all the code.  The test_warehouse() function runs through all functions separately and prints a success statement if all assets are checked. 



# Sports Item Catalog

## Scope of Project
Develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## Why This Project?
Modern web applications perform a variety of functions and provide amazing features and utilities to their users; but deep down, it’s really all just creating, reading, updating and deleting data. In this project, you’ll combine your knowledge of building dynamic websites with persistent data storage to create a web application that provides a compelling service to your users.

### Required software
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)

### To run test code
 *  Clone or download .zip of this repo
 *  Open terminal and cd into repo directory
 *  Run the following from terminal prompt
    1. `vagrant up` (this will take a while)
    2. `vagrant ssh` 
    3. `cd /vagrant/catalog`
    4. `python database_setup.py`
    5. `python database_seed.py` (load catagories and items)
    5. `python app.py`
 


##### TODO
* Add additional OAUTH providers

### Resources referenced
* [Udacity - The Backend: Databases & Applications](https://classroom.udacity.com/nanodegrees/nd004)
* [Flask Documentation](http://flask.pocoo.org/docs/0.12/)
* [Jinja Documentation](http://jinja.pocoo.org/docs/2.10/)
* [Google API Client Libraries](https://developers.google.com/api-client-library/python/)



# Credits

Vagrantfile copied from [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)
Alert: Sadly, I don't have time to maintain this.

Python Flask WEB API DEMO
========================
A full working flask demo api, exhaustive examples of common web services that we can made with this great micro-framework flask.
A kind of one-size-fits-all which can be too complicated for beginners and also too opinionated for advanced uses but first-of-all it's a full working example of common use cases in web api services featuring authentication and backoffice admin, resources CRUD and query pagination, modular structure, REST json responses or Html renders, bootstrap custom themes, some utils like config files for Nginx (as a frontend reverse proxy), Gunicorn (as a WSGI application server), Redis (as a server-side session storage), MySQL or SQLite (as DataBase) and much more features.

#### This is an advanced demo app forked from AndreiD/Flask-Easy-Template : https://github.com/AndreiD/Flask-Easy-Template
#### Additional reference sources - mbithenzomo/project-dream-team-three : https://github.com/mbithenzomo/project-dream-team-three


### Features:
	- configuration files, environment variables and sensitive variables (in private folder)
	- Production environment config : REDIS (as a server-side session storage), Nginx (as a frontend reverse proxy), Gunicorn (as a multi-threaded WSGI application server) and some supervisor (upstart) config file examples in utils folder
	- Utils for server production setups (nginx and supervisor config files for redis, gunicorn)
	- Latest bootstrap, bootswatch, modernizer, jquery, moment.js, tinymcs, etc. served from content delivery networks.
	- Module Sample PAGES, with home page  full-screen layout
	- Module Sample database SECTIONS with SQLALchemy, relational models and Pagination
	- Module Sample database USERS with SQLALchemy, relational models and Pagination
	- Module Sample page MESSAGES with email form, recaptcha and Email service by SendGrid and Flash MESSAGE notifications
	- Module Sample database RESOURCES :
								- ITEMS with images gallery and wysiwyg visual editor,
								- ASSETS files and image processing with Pillow
								- EVENTS (start/end datetime and timestamp operations)
								- ADDRESSES (google map and geocoding with latitude and longitude)
	- Module Sample database ORDERS and orderitem many-to-many relationship and shopping cart operations
	- Module Sample database PAYMENTS, credit cards, cryptography and transaction operations via paypal API Restful.
	- Module sample ADMIN, backoffice member with authentication  and authorization, and hash password powered by Flask-login and Werkzeug.security plugin :
			- User Registry, Login & Logout
			- Session based authentication or Basic HTTP authentication or Token based authentication (with active SSL recommended in production environement)
			- Password hash and password-check with werkzeug.security (bcrypt-like approach) (with active SSL recommended in production environment)
			- password base64 encoding for remote ajax-based app client (optional)
			- Role management (is_admin, is_owner, is_member), control access and Dashboard sample page.
	- SQLite or MySQL database configuration option
	-  SQL schema files and SQL populate files for SQLite or MySQL
	- ORM Schema relationships samples with SQLAlchemy :
		- ONE-TO-MANY and MANY-TO-ONE
		- HIERARCHIC (Adjacency List Relationships : parent-children)
		- MANY-TO-MANY Association object
	- CUSTOM THEME layout and templates
	- Logger setting service
	- INTERNATIONALIZATION with functions like get_locale() and get_timezone() (flask-babel optional) based on :
						current_user locale and current_user timezone
						or global current_language  and global timezone
						or browser language  and locale timezone
	- Helpers (include decorators like SSL required, threaded function, Datetime and timezone utils, datetime format filter, random populate data, Random token generator)
	- Maintenance/coming-soon, flash-message page
	- Error handlers :  404 (path not found),
						500 (server error),
						403 (forbidden page or invalid csrf token form),
						400 (Bad request, the syntax of the request entity is not correct),
						422 (Unprocessable Entity : the request is syntactically correct but his contained instructions is
							semantically erroneous so it was unable to process )


#### Security :
	You may have some sensitive variables that should not be publicly shared, such as passwords and secret keys.
	These can be put in an instance/config.py file, which will not be pushed to version control.
	(Flask default dedicated folder for secret data must be named /instance)
	Edit example config files in `utils` folder ( `prod-config.py`, `dev-config.py`, `test-config.py` )
	and move it to `/instance` folder, they will override some default variables in your `config.py` file.

#### How to use it:

	- `git clone https://github.com/systemaker/flask-web-api-demo.git <project_name>` or download the zip
	- `pip install -r requirements.txt` or `python -m pip install -r requirements-pip2.txt`
	- `python run.py` -> http://server_ip:5000

	- Troubleshoots or advanced python setup required ? 
	for PYTHON VIRTUAL ENVIRONMENT SETTING, see next section below.

#### Use it with configuration environment variable :
	- `export FLASK_CONFIG=production`
		or on Windows systems shell script `set FLASK_CONFIG=production`
	- `export FLASK_APP=run.py`
		or on Windows systems `set FLASK_APP=run.py`
	- `flask run`

##### Customize config:
	- check the `config.py`file  or your secret config `instance/config.py` file.
	Edit also example config files in `utils` folder ( `prod-config.py`, `dev-config.py`, `test-config.py` )
	and move it to `/instance` folder, they will override some default variables in your `config.py` file.

##### Customize templates edit `/app/templates/base.html`:

		> <!DOCTYPE html>
		> {% set bootstrap_version = '3.3.4' %}
		> {% set jquery_version = '2.1.3' %}
		> {% set modernizer_version = '2.8.3' %}
		> {% set bootswatch_version = '3.3.2' %}
		> {% set bootswatch_theme = 'slate' %}

		In case you don't like the "slate" theme, you can chose a nice theme from http://bootswatch.com/ and just replace the theme name

##### authorization control acces with Flask-login :
			- in template, use current_user  : {% if current_user.is_authenticated %} ... {% else %} ... {% endif %}
			- in controllers route, use `@login_required` to check if user is already login then  `current_user` to check his role
								from flask_login import login_required, current_user
								@auth_page.route('/dashboard')
								@login_required
								def dashboard():
									# prevent non-admin roles from accessing the page
									if not(current_user.is_admin):
										abort(403)
									return render_template('auth/dashboard.html')


---------------------------------------------------------------------------------------------------------
--------------  SECTION PYTHON VIRTUAL ENVIRONMENTS SETTING
---------------------------------------------------------------------------------------------------------

#### About python virtual environment : how to manage it in local project directory:

	# INSTALL VIRTUAL ENV : In Python 3.3, virtualenv is already included  !!! But his name is now pyvenv
		`pip install virtualenv`
		# optional switcher/wrapper helper `pip install virtualenvwrapper`
		# optional addon helper for windows `pip install virtualenvwrapper-win`
			- on Windows systems you can add an environment variable WORKON_HOME to specify the path to store environments (By default, this is %USERPROFILE%\Envs) ; pywin python version switcher is not included

	# List all of the environments
		`lsvirtualenv`

	# Create the directory ('/envs' for example if not exist) for the virtual environments for this project
		`mkdir /path/to/your_projet/envs`
	# Create your first virtual environnement for this project ('/libs1' for example )
		`virtualenv /path/to/your_projet/envs/libs1`
			or 'mkvirtualenv' ?
		# optional for no system libraries : --no-site-packages
		# optional for python version choice --python=your_python_path : -p /usr/bin/python2.6
				- to get python path : which python3
	# Activate this environment for your current shell session
		`workon [<name>]`
		or `source my_project/bin/activate`
		or on Windows go in the Scripts path folder `cd my_project/env/libs1/Scripts` then  `activate`

		- WARNING ON WINDOWS SYSTEMS : Some paths within the virtualenv are slightly different on Windows: scripts and executables on Windows go in ENV\Scripts\ instead of ENV/bin/ and libraries go in ENV\Lib\ rather than ENV/lib/.
			on Windows systems, the equivalent activate script is by opening active shell in the Scripts folder (Based on your active shell (CMD.exe or Powershell.exe), Windows will use either activate.bat or activate.ps1)

	# then install your dependencies
		`pip install -r requirements.txt` or `python -m pip install -r requirements-pip2.txt`

	# Deactivate the current working virtualenv and switch back to the default system Python.
		(myenv)$ `deactivate`
	# Remove a virtual environment
		`rmvirtualenv [<name>]`

##### To install a new package and save it on requirement file:
	`python -m pip install <new_package> && pip list > requirements.txt && pip list --format=freeze > requirements-pip2.txt`

##### To install all packages:
	`pip install -r requirements.txt` or `python -m pip install -r requirements-pip2.txt`

##### To remove all pyc files :
	`find . -name \*.pyc -delete`
	or for windows users  `del /S *.pyc`

---------------------------------------------------------------------------------------------------------
--------------  SECTION PRODUCTION ENVIRONMENT SETTING WITH REDIS, NGINX AND GUNICORN
---------------------------------------------------------------------------------------------------------

##### Extra configs for your server production environment : ./utils
	with nginx config files and supervisor (upstart) configuration  files for gunicorn

#### PRODUCTION CONFIG with GUNICORN : Use it for production with GUNICORN Upstart script and NGINX config from utils directory :

	- set environment to production with `export FLASK_CONFIG=production`
		or on Windows systems shell script `set FLASK_CONFIG=production`
	- active your Python virtual environment
	- GUNICORN : on shell command type  `gunicorn --bind 0.0.0.0:5000 run:app`
		'run' is the name of your main application file 'run.py'  which serve as the entry point for your application
		'app' is here the name of your defined application in app/__init__.py
	- If you visit your server's domain name or IP address with :5000 appended to the end in your web browser, you should see the homepage of your application
	- Create an Upstart script which will allow server to automatically start Gunicorn and serve our Flask application whenever the server boots :
					- create Gunicorn Upstart script : `sudo nano /etc/init/myproject_gunicorn.conf`
					or customize Upstart script file (edit example in file 'myproject_gunicorn.conf' in utils directory and replace 'myproject' paths by your project path) (replace user keyword by your chosen server user name ) and place it in /etc/init/myproject_gunicorn.conf
					- then type `sudo start myproject_gunicorn` (replace myproject with your application folder name)
					- After editing a code, you can refresh app by typing `sudo service myproject_gunicorn restart`
					- NOTE : with our Gunicorn config upstart script file, you can generate Python and Gunicorn error logs file and access logs file in your project folder 'myproject/logs'
### NGINX CONFIG :
	- NGINX:  then create a new server block configuration file in Nginx's sites-available directory.
		`sudo nano /etc/nginx/sites-available/myproject`
	- then customize it : see example in file 'utils/myproject_nginx.txt' in utils directory
	- Then enable the Nginx server block configuration,  link the file to the sites-enabled directory:
	`sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled`
	- test for syntax errors by typing: `sudo nginx -t`
	- restart the Nginx process to read the our new config: `sudo service nginx restart`

### REDIS CONFIG FOR SERVER-SIDE SESSION WITH FLASK SESSION and redis python extension :
	- Install, configure and secure Redis in your server : https://redis.io/
	- Add in your config.py file or prod-config.py file  :
			import redis
			...
			SESSION_TYPE = 'redis'
			SESSION_REDIS = redis.from_url('127.0.0.1:6379')


#### CORS CONFIG FOR FRONTEND WEB APP :
	- edit origins url in "register cors" section in __init__.py file :
		CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


---------------------------------------------------------------------------------------------------------
--------------  SECTION SQL DATABASE (MYSQL OR SQLite)
---------------------------------------------------------------------------------------------------------

#####  Customize database :
		# Edit sql file in `/data` folder

#### COMMON SQL SCRIPT ON DATABASE FROM MYSQL SERVER :
	- Signin  in first with `mysql -u root -p`
	- Create a database : `CREATE DATABASE my_database;`
	- Show all databases : `SHOW DATABASES;`
	- Select my database :  `USE my_database;`
	- Execute script on my database, for example  insert data into a mysql table :
		`INSERT INTO table_name (field1, field2, ...) VALUES (value1, value2, ...);`
	- Import and execute sql script file :
		`source /home/myproject_path/data/schema_mysql.sql;`
	- View current database : `SELECT database();`
	- Delete my database : `DROP DATABASE my_database;`


#### IMPORT SQL SCHEMA DATABASE SAMPLE IN MYSQL:
	`mysql -u root -p DB_NAME < /home/myproject_path/data/schema_mysql.sql`

#### EXPORT SQL SCHEMA DATABASE FROM MYSQL:
	`mysqldump -u root -p --databases DB_NAME > /home/myproject_path/data/schema_mysql.sql`



---------------------------------------------------------------------------------------------------------
--------------  SECTION TROUBLESHOOTS
---------------------------------------------------------------------------------------------------------

##### TROUBLESHOOTS FOR BEGINNERS :

    - READ FIRST : About Python 2 and 3 compatibility
    Some scripts and modules versions required here are written in python 2 and not ready yet for python 3 , 
    so it is recommended to download and install both interpreters python 2 and also python 3 (for windows users don't forget to add their folder paths also in your environment variables)
    Then when calling python scripts in version 2 or 3 anyway (example with the package manager script PIP), you can run default python command like :
        "python -m pip install ..." or "pip install ..."
    To call only python 3 scripts choose  this  instead :
        "py -m pip install ..." or "pip3 install ..."
	-----------------------------------------------------------------------------------------

    - Error parsing in requirements.txt ?
        Run instead this compatible formatted file :
            python -m pip install -r requirements-pip2.txt
        or convert first your requirements.txt to a python 2 pip2 compatible format with this command :
            python -m pip list --format=freeze > requirements.txt

	-----------------------------------------------------------------------------------------
    - Error install on Proxytype : SyntaxError like Missing parentheses in call to 'print' ?
        the print function requires parentheses in Python 3 but not in Python 2 which means that the extension that you are trying to install is not yet compatible with python 3
        This is why it is recommended to install python 3 and python 2 by default.
        So run instead this compatible command for python 2 extensions (after installing python 2 if not got it yet) :
            python -m pip install -r requirements-pip2.txt
            or python -m pip install ...
	-----------------------------------------------------------------------------------------

    - Error install module Pycrypto : microsoft visual c++ compiler for python 2.7  is required ?
        download and install microsoft visual c++ compiler for python 2.7 here : https://www.microsoft.com/en-us/download/details.aspx?id=44266

	-----------------------------------------------------------------------------------------
    - Error Tornado module not found ?
        it is a problem when installing modules like tornado in a multiple python interpreters environment
        So run instead this common command python which precize by default  the python 2 version
            python -m pip install -r requirements-pip2.txt
            or python -m pip install ...
            or python run.py

    - Error Install MySQL-python on Windows systems not working ?
        go over to oracle, and download the MySQL Connector C 6.0.2 and do the typical install.
        http://dev.mysql.com/downloads/connector/c/6.0.html#downloads


Your Feedback is appreciated :)

##### License: Apache 2.0

~~~~
Copyright 2017 Systemaker.com

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
~~~~
limitations under the License.

# prompts_manager
## About
This prompts manager allow a user to add, edit, delete and manage writing prompts.

Prompts can be sorted by collections.

Prompts can be scraped from AO3's writing exchanges tagsets, for instance [here](https://archiveofourown.org/tag_sets/10303). Any prompt set in the tagset's Original category (or equivalent thereof if the exchange follows the most common naming rules) will be scraped and added to the user's own.

## Libraries & tools
As this app was created for training, I've chosen to use tools I was less familiar with but which made sense for the project's scope:

* **[Flask](https://flask.palletsprojects.com/) is a lightweight web framework which uses the Jinja template engine and the Werkzeug WSGI toolkit**. Though more flexible than Django (a more complete framework, but also a more opinionated one), its emphasis on user agency means that I had to be more careful about secure code.

* **[SQLite3](https://docs.python.org/3/library/sqlite3.html) is a Python library using SQLite, a lightweight disk-based database which can be accessed using the SQL language**. Its main advantages are its ease of use, which makes it a popular choice for prototyping: as it is disk-based, it doesn't have to be hosted on a server (whether locally of not) and can be easily edited or copied. Furthermore, it's part of the Python standard library.

* **[Unittest](https://docs.python.org/3/library/unittest.html) is a class-based Python library used for testing**, and one of the most used in Python environments. As part of the Python standard library, it allows us to keep our app lightweight.

Though the app as it is could have been coded with a GUI library such as Tkinter or Qt, I wished to make it web-based so that I could potentially develop it into a full multi-users website. 

## Usage
Clone the repository, then [set up and activate your virtual environment](https://docs.python.org/3.10/library/venv.html).

Still using your console, install the required external packages with the command `pip install -r requirements.txt`.

Then, at the same level as the .app folder, create a file named `.env` and a file named `.flaskenv`. Inside `env`, indicate a secret key like so:

```
SECRET_KEY='MY_SECRET_KEY'
```

Inside `.flaskend`, set these two variables like so:

```
FLASK_APP=app/app.py
FLASK_DEBUG=True
```

Then, either simply type `flask run` (since you set up the path to the app in `.flaskenv`) or navigate to the `app` folder and use the command`flask --app app run`. If you want to deactivate debug mode, you can set up FLASK_DEBUG to False.

The server will launch and you'll see an URL mentioned in the console (it should be http://127.0.0.1:5000/, but don't be alarmed if this is different). Access it with your navigator of choice.

## Credits
Site icon by [Afian Rochmah Afif](https://www.flaticon.com/authors/afian-rochmah-afif)
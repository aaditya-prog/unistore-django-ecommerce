To run the project, you must have python installed on your system. Download the latest version of
python from the [Download Python](https://www.python.org/downloads/) page.

For packaging and dependency management of the application, python poetry has
been used. So, the second step is to install poetry on your system.

>Install poetry using the command `pip install poetry`. If you are facing
any problems installing and using poetry, read the docs here. [Poetry Docs](https://python-poetry.org/docs/)

You don't need to run the project in a virtual environment as poetry will automatically create a
virtual environment on your system. Now go to your terminal, type `poetry run python manage.py check`.
If you don't see any errors, you can run the server by typing `poetry run python manage.py runserver`.

You should be good to go now.

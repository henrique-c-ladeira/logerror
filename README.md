# Error Logs Application

![badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![badge](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

This project is a web admin interface to list error logs from other applications. You can create an error log sending a POST request to the '/log' API url. This app relies on the built in Django's admin interface.

Contributions are welcome. 🌟

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Prerequisites

You need python3 to build the virtualenv and install the required libraries.

You may also need mysql installed (unless you tweek `'logerror/settings.py'` to use sqlite and remove mysqlclient from `'requirements.txt'`)

### Installing

After clonning the repository copy `'/logerrror/.env.template'` file at the same folder and rename it to `'.env'`. Then set the variables according to your MySQL dabatabase.

    DB_NAME=database_name
    DB_USER=database_user
    DB_PASSWORD=my_secret_password
    DB_HOST=host_address
    DB_PORT=database_port
    DEBUG=1
    SECRET_KEY=your_secret_key_for_django

Before you install the required pip packages, you need to have mysql installed, if you are on macOS this can be achieved by running:

```sh
brew install mysql
```

You can install the app by executing the `'install.sh'` script if you are on Linux or Mac. On windows you have to create a python 3 virtual enviroment at `'.venv/'` in the project root folder and install the pip packages at `'requirements.txt'`.

## Running the app

After installing it, make sure the virtual environment is activated. There is a symlink pointing to `'.venv/bin/active'` at the project root folder.

```
source activate
```

After that you are good to go!

Run the development server by executing

```
django r
```

or if you prefer the no-shortcut command:

```
python manage.py runserver
```

Also you can generate a random secret key for the SECRET_KEY env variable, just type at the terminal

```
python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'
```

## Create errors API

To create an error just send a `POST` request to `'{url}/log/'` i.e.:

```HTTP
# url_example = http://127.0.0.1:8000/log/

POST /log/ HTTP/1.1
Content-Type: application/json
Host: 127.0.0.1:8000

{
	"app_name": "Mega App",
	"stack": "Component Stack: in LandingPage (at SceneView.tsx:126)in StaticContainer in EnsureSingleNavigator (at SceneView.tsx:118) in SceneView (at useDescriptors.tsx:209) in RCTView (at View.js:34) in View (at createAnimatedComponent.js:217) in AnimatedComponent (at createAnimatedComponent.js:278) in AnimatedComponentWrapper (at BottomNavigation.tsx:649)",
	"message": "Infelizmente o negócio quebrou aí."
}
```

## Deployment

The system is ready to be deployed on Heroku.

    Follow the instructions at: https://devcenter.heroku.com/articles/git

Remember to set the enviroment variables and also set **DEBUG=0**.

<!-- ## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us. -->

<!-- ## Versioning

We use [Semantic Versioning](http://semver.org/) for versioning. For the versions
available, see the [tags on this
repository](https://github.com/PurpleBooth/a-good-readme-template/tags). -->

## License

MIT

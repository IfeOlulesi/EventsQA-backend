# Events QA
Ever wanted to host a QA event and needed an efficient way to receive questions from the attendees?

Events QA makes this easy for you!

## Features
- Create events with a few button clicks
- Receive questions from your attendees (optionally anonymous)


## Setup

STEP 1: Clone the repository:

```sh
$ git clone []
# $ cd ToDo-App-Django
```

STEP 2: (Optional but Recommended) Create a virtual environment to install dependencies in and activate it:

```sh
$ py -m venv .venv
$ source env/bin/activate (Mac) OR venv\\bin\\activate (Windows)
```

STEP 3: Install the dependencies:

```sh
$ pip install -r requirements.txt
```
If you followed STEP 2, you should see an `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

STEP 4: Once `pip` has finished downloading the dependencies, run the following in your terminal:

```sh
$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`

To play around with the API, run
```
(env)$ python manage.py shell
```
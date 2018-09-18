# world\_challenge\_web
World Challenge Web Application

### Development
A simple development workflow while things are small.

To get started, follow these steps:

1. Clone down the repo
```bash
git clone git@github.com:worldchallenge/world_challenge_web
```
2. Change directory into the `world_challenge_web` project you just cloned locally.
```bash
cd world_challenge_web/
```
3. Create and source a new python virtual environment
```bash
python3 -m venv env
source env/bin/activate
```
4. Install pip deps
```
pip install -r requirements.txt 
```
5. Create migrations for custom user model
```bash
./manage.py makemigrations world_challenge_user_profile
```
6. Perform migrations
```bash
./manage.py migrate
```
7. Create superuser
```bash
./manage.py createsuperuser
```
8. Start development webserver
```bash
./manage.py runserver 0.0.0.0:8000
```

### Basic Login and Logout process

Simple templates are used until style and design are agreed upon.

1. Homepage located at 127.0.0.1:8000/home/ consists of a single link to Login.

2. Login takes you to a page that requests Username and Password with a url http://127.0.0.1:8000/accounts/login/.  If the information is not verified a message "Your username and password didn't match. Please try again." is given.  If successful, the user is taken to http://127.0.0.1:8000/accounts/profile/.  This page so far only shows that authentication is successful and will be developed further.  The Login page also has a Lost Password link that leads to http://127.0.0.1:8000/accounts/password_reset/ and gives a very simple opportunity to Reset Password.

3. The Profile page has a link enabling the user to Logout.

### Event framework

1. New events are created and listed in a common area.

2. The ability to update existing events.
      - Only the owner is authorized to make changes on events created by them.

3.  Individual event pages are selectable through event listing page.

4.  Each event has the ability to be voted on. 
      - Users are only able to vote once per event.  
      - Votes can be rescinded by the voter.
      - Votes can be aggregated by total and user.


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


Simple templates are used until style and design are agreed upon.

1. Homepage located at 127.0.0.1:8000/ 


### Profile framework

1. Individual selects the "SignUp" tab top left corner.

2. User enters username, email and password.

3. Email is sent for verification and user selects link to be validated.

4. User is now able to log in.

5. Under Profile is a tab "List Profiles" which show all Profiles created thus far.  Profiles are able to be viewed by all.

6. If user selects their own profile it will show the ability to update.  Only users own profile is eligible for update.

7. Fields available so far: first name, last name, bio, location and birthdate.  Avatars will be added later.


### Event framework

1. New events are created and listed in a common area.

2. The ability to update existing events.
      - Only the owner is authorized to make changes on events created by them.

3.  Individual event pages are selectable through event listing page.

4.  Each event has the ability to be voted on. 
      - Users are only able to vote once per event.  
      - Votes can be rescinded by the voter.
      - Votes can be aggregated by total and user.



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

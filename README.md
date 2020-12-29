# exercisetracker
An opportunity to learn React and make a useful exercise journal

# Setup

<b>Note</b>: Ensure you're using Python 3.6.2 in your virtual environment

1. Clone the repository
2. `cd` into the cloned folder
3. Create a new virtual environment with `virtualenv venv` (if you need help with this step: refer to: https://virtualenv.pypa.io/en/latest/)
4. Activate your virtual environment
5. `cp env.example .env` and change the SECRET_KEY
6. Source the `.env` file
7. `pip install -r requirements.txt`
8. `python manage.py migrate`
9. `python manage.py createsuperuser` and follow prompts
10. `python manage.py runserver`
11. Develop the frontend inside of `frontend/src/`
12. In `frontend/src` run `npm run start:dev` (both servers must be running for hot reloading to work)

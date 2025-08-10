School SMS - Prefilled Admin Demo

This package has admin credentials prefilled in .env for an immediate demo.

Default admin credentials:
- Username: admin
- Email: admin@schooldemo.ke
- Password: AdminPass2025

Quick local setup:
1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py loaddata core/fixtures/initial_data.json
6. python create_admin.py  # creates the admin user using .env values
7. python manage.py runserver

Deploy to Render: push to GitHub, create web service, set build command to:

pip install -r requirements.txt && python manage.py migrate --noinput && python create_admin.py

Then start with Procfile.

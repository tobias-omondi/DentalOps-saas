# DentalOps-saas
DentalOps is a SaaS product used by dentists to track patient data, such as medical history. The problem that the app is solving is to automatically send messages to patients through SMS/email if they have not been to the clinic in more than 3 months. Over 33% of dentists report insufficient patient retention, with patients who walk away and never return to their clinics. It's a micro-SaaS that uses AI to send messages to follow up for specific procedures.

## Features
- Patient data tracking
- Automated SMS/email messaging
- AI-powered follow-up messages
- Procedure-specific reminders

## INSTALLATION
    cd myprojectname
    cd backend
### virtual eniviroment
    python3 -m venv env
### Activate
    source venv/bin/activate

    pip install django djangorestframework
    django-admin startproject myproject
    cd myproject
### creating new app in my project
    python manage.py startapp myapp
### run dev
    python manage.py runserver


## Tech languange use
    python3 (django and django rest framework)
    postgresssql

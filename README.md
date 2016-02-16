# Contact Info

Contact info is a simple Django app to manage address data.

Detailed documentation is in the "docs" directory.

## Installation

`npm install https://s3-us-west-2.amazonaws.com/nrose-django-packages/django-contact_info-0.1.2.zip`

## Usage

1. Add `contact_info` to `INSTALLED_APPS` setting:
```python
# yourapp/settings.py
# ...
    INSTALLED_APPS = (
        ...
        'contact_info',
    )
```
2. There are no front-end URLs defined for the package.
3. Run `python manage.py migrate` to create the contact info models.
4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create an address (you'll need the Admin app enabled).
5. Intended as a way to quickly add standardized contact info models across Django projects.
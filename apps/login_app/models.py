from __future__ import unicode_literals
from django.db import models
from ..car_app.models import Car
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def registerVal(self, postData):
        results = {'status': False, 'errors': []}

        if len(postData['first_name']) < 3:
            results['errors'].append('First name must be at least 3 characters.')
            results['status'] = True

        if len(postData['last_name']) < 3:
            results['errors'].append('Last name must be at least 3 characters.')
            results['status'] = True

        if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
            results['errors'].append('Please enter a valid email.')
            results['status'] = True

        if len(postData['password']) < 5:
            results['errors'].append('Password must be at least 5 characters.')
            results['status'] = True

        if postData['password'] != postData['con_password']:
            results['errors'].append('Password must match.')
            results['status'] = True

        if results['status'] == False:
            if len(self.filter(email = postData['email'])) == 0:
                hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
                results['user'] = self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], birthdate = postData['birthdate'], password = hashed)
            else:
                results['errors'].append('User already exists.')
                results['status'] = True

        return results

    def loginVal(self, postData):
        results = {'status': False, 'errors': [], 'user': None}
        user = self.filter(email = postData['email'])

        if len(user) < 1 or not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
            results['errors'].append('Something went wrong. Check your login credentials and try again.')
            results['status'] = True
        else:
            results['user'] = user[0]

        return results



class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 255)
    birthdate = models.DateField()
    cars_owned = models.ManyToManyField(Car, related_name = 'user_owner')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

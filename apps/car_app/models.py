from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CarManager(models.Manager):
    def carVal(self, postData):
        results = {'status': False, 'errors': []}

        if not postData['make'] or len(postData['make']) < 1:
            results['errors'].append('Make of car must be at least 1 character long.')
            results['status'] = True

        if not postData['model'] or len(postData['model']) < 1:
            results['errors'].append('Model of car must be at least 1 character long.')
            results['status'] = True

        if not postData['year'] or len(str(postData['year'])) < 4:
            results['errors'].append('Year of car must be in YYYY form.')
            results['status'] = True

        if results['status'] == False:
            if len(self.filter(make = postData['make'], model = postData['model'], year = postData['year'])) == 0:
                results['car'] = self.create(make = postData['make'], model = postData['model'], year = postData['year'])
            else:
                results['errors'].append('Car has already been added.')
                results['status'] = True

        return results


class Car(models.Model):
    make = models.CharField(max_length = 100)
    model = models.CharField(max_length = 100)
    year = models.CharField(max_length = 100)

    objects = CarManager()

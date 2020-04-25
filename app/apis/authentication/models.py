from django.db import models
import uuid

class UserModel(models.Model):
    '''Defines attributes of the payments model'''
    STATUS = [
        ('O', 'Ok'),
        ('P', 'Pending'),
        ('C', 'Cancelled')
    ]
    id = models.CharField(db_index=True, max_length=255,
                          unique=True, primary_key=True)
    name = models.CharField(db_index=True, max_length=15)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        default='P',
    )

    def __str__(self):
        return self.status

    def save(self,*args, **kwargs): # pylint: disable=W0221
        uuid_ = uuid.uuid4().hex
        # This to check if it creates a new or updates an old instance
        if not self.id:
            self.id = uuid_
        super(UserModel, self).save() # pylint: disable=W0221

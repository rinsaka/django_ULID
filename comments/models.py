import ulid
from django.db import models

# Create your models here.


class ULIDField(models.CharField):
    """ see https://qiita.com/ykiu/items/c288b99d0a1956e8ac9f """
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 26
        super(ULIDField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'char(26)'

class Comment(models.Model):
    id = models.CharField(
        default=ulid.new,
        max_length=26,
        primary_key=True,
        editable=False
    )
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

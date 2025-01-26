from django.db import models
from django.core.files.storage import FileSystemStorage
import os

class TableBasedStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        self.table_name = kwargs.pop('table_name', '')
        super().__init__(*args, **kwargs)

    def get_available_name(self, name, max_length=None):
        # Generate the path dynamically based on table name or other fields
        table_folder = self.table_name
        name = os.path.join(table_folder, name)
        return super().get_available_name(name, max_length)

# Create your models here.
class blogs(models.Model):
    title=models.CharField(blank=False,max_length=100,unique=True)
    img=models.URLField()
    des=models.TextField()
    link=models.URLField(blank=False)
    words=models.CharField(max_length=255,null=True)
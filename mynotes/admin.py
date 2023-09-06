from django.contrib import admin

# Register your models here.
from .models import Mynotes   # we can add
#here the class nname which we create in model.py

## and for adding into the websites simply we
# need to regiser
admin.site.register(Mynotes)

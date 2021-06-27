from django import forms
from django.db.models import fields
from django.forms import ModelForm
from dongi.models import user   

class userf (ModelForm):
    class Meta:
        model = user
        fields = ["id","first_name","last_name"]
        lables = {'first_name':"First name",'last_name':"Last name"}
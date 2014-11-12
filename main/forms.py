# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


class AddForm(forms.Form):
    table1_id = forms.IntegerField()
    table2_id = forms.IntegerField()
    field5 = forms.CharField()

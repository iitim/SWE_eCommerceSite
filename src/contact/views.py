# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def contact(request):
    context = locals()
    template = 'contact.html'
    return render(request, template, context)
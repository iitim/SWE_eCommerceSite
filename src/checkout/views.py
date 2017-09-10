# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def checkout(request):
    context = {}
    template = 'checkout.html'
    return render(request, template, context)
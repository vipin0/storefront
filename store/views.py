from django.db.models import Q,F, Value,Func
from django.db.models.aggregates import Count, Min, Max, Avg
from django.shortcuts import render
from django.db.models.functions import Concat

from store.models import Customer, Product
# Create your views here.


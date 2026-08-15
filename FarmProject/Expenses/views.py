from django.shortcuts import render
from rest_framework import viewsets
from .models import Expenses
from .serializers import ExpensesSerializer

class ExpensesViewSet(viewsets.ModelViewSet):
    queryset=Expenses.objects.all()
    serializer_class=ExpensesSerializer

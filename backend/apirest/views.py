from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from backend.apirest.serializers import PrinterSerializer


class PrinterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows printers to be viewed or edited.
    """
    queryset = Printer.objects.all().order_by('-date_joined')
    serializer_class = PrinterSerializer
    permission_classes = [permissions.IsAuthenticated]
    
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .serializers import CertSerializer
from .models import Cert
import subprocess
import os


# from .mixin import CertMixin

# Create your views here.
class CertView(viewsets.ModelViewSet):
    # class CertView(CertMixin, viewsets.ModelViewSet):
    queryset = Cert.objects.all()
    serializer_class = CertSerializer

    def get_queryset(self):
        # print("???? query set")
        # print(self.request.GET)
        query_id = self.kwargs["pk"]

        if query_id:
            print(query_id)
            ROOT_DIR = os.path.abspath(os.curdir)
            print(ROOT_DIR)
            var = subprocess.Popen(
                ["sh", "../test.sh"],
                stdout=subprocess.PIPE,
            )
            print("???? print var")
            print(var.communicate())

        return self.queryset.all()

    # CertMixin.gen_cert()
    # serializer_class = CertSerializer
    # queryset = Cert.objects.all()

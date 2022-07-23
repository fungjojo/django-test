from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import CertSerializer
from .models import Cert
import subprocess

# import os

# Create your views here.
class CertView(viewsets.ModelViewSet):
    queryset = Cert.objects.all()
    serializer_class = CertSerializer

    def create(self, request):

        # get latest nonce
        query_results = Cert.objects.latest("nonce")
        latest_nonce = query_results.nonce
        print("latest nonce=%s", latest_nonce)

        # issue cert
        # ROOT_DIR = os.path.abspath(os.curdir)
        # print("ROOT_DIR=%s", ROOT_DIR)
        var = subprocess.Popen(
            ["sh", "../test.sh", str(latest_nonce)],
            stdout=subprocess.PIPE,
        )
        output = var.communicate()
        print("???? output =%s", output)

        # POST and update serializer
        newData = request.POST.copy()
        newData["nonce"] = 11
        newData["nonce"] = latest_nonce + 1

        print("???? newData =%s", newData)
        serializer = self.get_serializer(data=newData)
        serializer.is_valid(raise_exception=True)
        super().perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=200, headers=headers)

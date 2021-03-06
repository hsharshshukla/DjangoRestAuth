# from django.shortcuts import render
# Create your views here.

from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User

class UserRecordView(APIView):

    permission_classes = [IsAdminUser]

    def get(self,format=None):
        users=User.objects.all()
        # print(users)
        serializer=UserSerializer(users,many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,status=201
            )

        return Response(
            {
                "error":True,
                "error_msg":serializer.error_messages
            },
            status=400
        )


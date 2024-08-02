from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.shortcuts import get_object_or_404
from app.university.models import UniData
from app.university.serializers import UniDataSerializer
from app.university.utils import UniversityDataHandler


class FetchUniversityDataView(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        try:
            data=UniversityDataHandler.fetch_data()
            return Response({'data':data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)

class FetchAndStoreUniversityDataView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            UniversityDataHandler.fetch_and_store_data()
            return Response({'message':'Data fetched and stored successfully in databases'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)

class UniversityListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        universities=UniData.objects.all()
        serializer=UniDataSerializer(universities,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class UniversityDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,id):
        university = get_object_or_404(UniData,pk=id)
        serializer = UniDataSerializer(university)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        university = get_object_or_404(UniData,pk=id)
        serializer = UniDataSerializer(university,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, {'message':f'Data {id} has been updated'},status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        university=get_object_or_404(UniData,pk=id)
        serializer=UniDataSerializer(university,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,{'message': f'Data {id} has been updated'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        university=get_object_or_404(UniData,pk=id)
        university.delete()
        return Response({'message': f'Data {id} has been deleted'}, status=status.HTTP_200_OK)
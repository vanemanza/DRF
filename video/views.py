from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializers
from django.http import Http404

# Create your views here.
class ListaVideo(APIView):

    def get(self, request):
        videos = Video.objects.all()
        videos_json = VideoSerializers(videos,many=True)
        return Response(videos_json.data)

    def post(self, request):
        video_json = VideoSerializers(data=request.data)#deserialiizar?
        if video_json.is_valid():
            video_json.save()
            return Response(video_json.data, status=201)
        return Response(video_json.errors, status=400)
            
class DetailVideo(APIView):

    def get_object(self, pk):
            try:
                return Video.objects.get(pk=pk)
            except Video.DoesNotExist:
                raise Http404        

    def get(self, request, pk):
        video = self.get_object(pk)
        video_json = VideoSerializers(video)
        return Response(video_json.data)
        
    def put(self, request, pk):
        video = self.get_object(pk)
        video_json = VideoSerializers(video, data=request.data)
        if video_json.is_valid():
            video_json.save()
            return Response(video_json.data)
        return Response(video_json.errors, status=400 )    
              
    def delete(self, request, pk):
        video = self.get_object(pk)
        video.delete()
        return Response(status=204)

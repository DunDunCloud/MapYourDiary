from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from map.models import MapPost
from map.serializers import MapSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def post_list(request):
    if request.method == 'GET':
        map = MapPost.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            map = MapPost.filter(title__icontains=title)
        
        map_serializer = MapSerializer(map, many=True)
        return JsonResponse(map_serializer.data, safe=False)

    elif request.method == 'POST':
        map_data = JSONParser().parse(request)
        map_serializer = MapSerializer(data=map_data)
        if map_serializer.is_valid():
            map_serializer.save()
            return JsonResponse(map_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(map_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = MapPost.objects.all().delete()
        return JsonResponse({'message': '{} MapPosts were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        map = MapPost.objects.get(pk=pk) 
    except MapPost.DoesNotExist: 
        return JsonResponse({'message': 'The post does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    if request.method == 'GET': 
        map_serializer = MapSerializer(map) 
        return JsonResponse(map_serializer.data)

    elif request.method == 'PUT': 
        map_data = JSONParser().parse(request) 
        map_serializer = MapSerializer(map, data=map_data) 
        if map_serializer.is_valid(): 
            map_serializer.save() 
            return JsonResponse(map_serializer.data) 
        return JsonResponse(map_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': 
        map.delete() 
        return JsonResponse({'message': 'map was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def post_list_published(request):
    map = MapPost.objects.filter(published=True)
        
    if request.method == 'GET': 
        map_serializer = MapSerializer(map, many=True)
        return JsonResponse(map_serializer.data, safe=False)
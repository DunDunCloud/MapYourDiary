from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from map.models import PlacePost, PostLike, MapYourDiary
from map.serializers import PlacePostSerializer, LikeSerializer, MapYourDiarySerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        users = MapYourDiary.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            users = MapYourDiary.filter(title__icontains=title)
        
        users_serializer = MapYourDiarySerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    elif request.method == 'POST':
        users_data = JSONParser().parse(request)
        users_serializer = MapYourDiarySerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = MapYourDiary.objects.all().delete()
        return JsonResponse({'message': '{} MapPosts were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def diary_list(request):
    if request.method == 'GET':
        place_posts = PlacePost.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            place_posts = PlacePost.filter(title__icontains=title)
        
        place_post_serializer = PlacePostSerializer(place_posts, many=True)
        return JsonResponse(place_post_serializer.data, safe=False)

    elif request.method == 'POST':
        place_posts = JSONParser().parse(request)
        place_post_serializer = PlacePostSerializer(data=place_posts)
        if place_post_serializer.is_valid():
            place_post_serializer.save()
            return JsonResponse(place_post_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(place_post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = PlacePost.objects.all().delete()
        return JsonResponse({'message': '{} MapPosts were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def post_like_input(request):
    if request.method == 'POST':
        like_data = JSONParser().parse(request)
        like_serializer = LikeSerializer(data=like_data)

        if like_serializer.is_valid():
            like_serializer.save()
            return JsonResponse(like_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(like_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Post Like
@api_view(['GET', 'PUT', 'POST'])
def post_like(request, pk):
    # find tutorial by pk (id)
    try: 
        map = PostLike.objects.get(pk=pk) 
    except PostLike.DoesNotExist: 
        return JsonResponse({'message': 'The post does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    if request.method == 'GET': 
        like_serializer = LikeSerializer(map) 
        return JsonResponse(like_serializer.data)

    elif request.method == 'POST':
        like_data = JSONParser().parse(request)
        like_serializer = LikeSerializer(data=like_data)

        if like_serializer.is_valid():
            like_serializer.save()
            return JsonResponse(like_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(like_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT': 
        like_data = JSONParser().parse(request) 
        like_serializer = LikeSerializer(map, data=like_data) 
        if like_serializer.is_valid(): 
            like_serializer.save() 
            return JsonResponse(like_serializer.data) 
        return JsonResponse(like_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': 
        map.delete() 
        return JsonResponse({'message': 'map was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

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
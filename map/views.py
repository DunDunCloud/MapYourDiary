from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from map.models import User, Diary, Like
from map.serializers import UserSerializer, DiarySerializer, LikeSerializer
from rest_framework.decorators import api_view


# User 조회, 등록, 삭제
@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    # 모든 User 조회 (GET -> http://127.0.0.1/api/user)
    if request.method == 'GET':
        users = User.objects.all()
        # title = request.GET.get('title', None)

        # if title is not None:
        #     users = User.filter(title__icontains=title)
        
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    
    # User 등록 (POST -> http://127.0.0.1/api/user)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 모든 User 삭제 (DELETE -> http://127.0.0.1/api/user)
    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'MESSAGE!': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# Diary 조회, 등록, 삭제
@api_view(['GET', 'POST', 'DELETE'])
def diary_list(request):
    # 모든 Diary 조회 (GET -> http://127.0.0.1/api/diary)
    if request.method == 'GET':
        diary = Diary.objects.all()
        title = request.GET.get('title', None)

        if title is not None:
            diary = Diary.filter(title__icontains=title)
        
        diary_serializer = DiarySerializer(diary, many=True)
        return JsonResponse(diary_serializer.data, safe=False)
    
    # Diary 등록 (POST -> http://127.0.0.1/api/diary)
    elif request.method == 'POST':
        diary = JSONParser().parse(request)
        diary_serializer = DiarySerializer(data=diary)

        if diary_serializer.is_valid():
            diary_serializer.save()
            return JsonResponse(diary_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(diary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Diary 삭제 (DELETE -> http://127.0.0.1/api/diary)
    elif request.method == 'DELETE':
        count = Diary.objects.all().delete()
        return JsonResponse({'MESSAGE!': '{} All Diaries were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

# 좋아요 누른 Diary 조회, 등록
@api_view(['GET', 'POST'])
def like_list(request):
    # 좋아요 누른 Diary 조회 (GET -> http://127.0.0.1/api/like)
    if request.method == 'GET':
        like = Like.objects.all()
        title = request.GET.get('title', None)

        if title is not None:
            like = Like.filter(title__icontains=title)
        
        like_serializer = LikeSerializer(like, many=True)
        return JsonResponse(like_serializer.data, safe=False)

    # 좋아요 누른 Diary에 등록 (POST -> http://127.0.0.1/api/like)
    elif request.method == 'POST':
        like = JSONParser().parse(request)
        like_serializer = LikeSerializer(data=like)

        if like_serializer.is_valid():
            like_serializer.save()
            return JsonResponse(like_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(like_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 좋아요 누른 특정 Diary 조회, 등록
@api_view(['GET', 'PUT', 'POST'])
def post_like(request, pk):
    # find tutorial by pk (id)
    try: 
        like = Like.objects.get(pk=pk) 
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
# Rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from users.models import Profile
from users.serializer import *

@api_view(['GET', 'POST'])
def userProfiles_list(request):
    """List owner or create a new one"""

    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        userProfiles = Profile.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(userProfiles, 9)

        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = ProfileSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'page': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/users?page=' + str(nextPage), 'prevlink': '/api/users?page=' + str(previousPage)})
    
    elif request.method == 'POST':
        serializer = ProfileSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """Retrieve, update or delete a owner by id/pk"""

    try:
        owner = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(owner, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfileSerializer(Profile, data=request.data, context={'request': request})
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
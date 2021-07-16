# Rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from walkers.models import Walker
from walkers.serializer import *

@api_view(['GET', 'POST'])
def GET_POST_USER(request):
    """List walkers or create a new one"""

    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        userProfiles = Walker.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(userProfiles, 9)

        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = WalkerSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'page': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/walkers?page=' + str(nextPage), 'prevlink': '/api/walkers?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = WalkerSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def GET_PUT_DELETE_USER(request, pk):
    """Retrieve, update or delete a walker by id/pk"""

    try:
        walker = Walker.objects.get(id=pk)
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WalkerSerializer(walker, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WalkerSerializer(Walker, data=request.data, context={'request': request})
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        walker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
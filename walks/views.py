from walkers.models import Walker
from walks.models import Walk

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import WalkReadSerializer, WalkCreateSerializer, WalkUpdateSerializer
from walkers.serializer import WalkerSerializer

@api_view(['GET', 'POST'])
def GET_POST_WALK(request):

    if request.method == 'GET':
        walks = Walk.objects.all()
        serializer = WalkReadSerializer(walks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WalkCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def GET_PUT_DELETE_WALK(request, pk):
    """Retrieve, update or delete a walker by id/pk"""

    try:
        walk = Walk.objects.get(id=pk)
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WalkReadSerializer(walk, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WalkUpdateSerializer(walk, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        walk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def GET_WALKS_BY_WALKER(request, pk_walker):
    try:
        walks = Walk.objects.filter(walker_id=pk_walker)
    except Walk.DoesNotExist:
        return Response({"error": "El paseo no existe"});

    try:
        walker = Walker.objects.get(id=pk_walker)
    except Walker.DoesNotExist:
        return Response({"error": "El paseador no existe"});

    walks_serializer = WalkReadSerializer(walks, context={'request': request}, many=True)
    walker_serializer = WalkerSerializer(walker, context={'request': request}, many=False)

    return Response({'data': {'walker': walker_serializer.data, 'walks': walks_serializer.data }}, status=status.HTTP_200_OK)
    

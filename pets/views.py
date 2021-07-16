from rest_framework import status
from users.serializer import ProfileSerializer
from users.models import Profile
from pets.models import Pet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PetSerializer

@api_view(['GET', 'POST'])
def getPost_pet(request):

    if request.method == 'GET':
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
def deletePostGet_pet(request, pk):
    try:
        pets = Pet.objects.get(id=pk)
    except Pet.DoesNotExist:
        return Response(data={"error": "Mascota no encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        pets.delete()
        return Response("Pet succesfully deleted!")

    elif request.method == 'PUT':
        serializer = PetSerializer(instance=pets, data=request.data, partial=True)

        print(serializer)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)
    
    elif request.method == 'GET':
        serializer = PetSerializer(pets, many=False)
        return Response(serializer.data)


@api_view(['GET'])
def get_pets_by_owner(request, pk_user):
    pets = Pet.objects.filter(user_id = pk_user)
    user = Profile.objects.get(id = pk_user)

    pet_serializer = PetSerializer(pets,context={'request': request}, many=True)
    owner_serializer = ProfileSerializer(user, context={'request': request}, many=False)
    return Response({'data': {'owner': owner_serializer.data , 'pets': pet_serializer.data}}, status=status.HTTP_200_OK)
    
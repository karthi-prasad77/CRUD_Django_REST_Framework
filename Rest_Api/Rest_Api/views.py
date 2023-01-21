from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# creating endpoints
# Get functionality
# pass methods in a list
@api_view(['GET', 'POST'])
def drink_list(request):
    """
    Get all the drinks
    serialize them 
    reurn it into JSON format
    """
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many = True)   # all fields
        return JsonResponse({'drinks': serializer.data})
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data = request.data)
        # check for the valid data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
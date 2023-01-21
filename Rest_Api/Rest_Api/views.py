from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

# creating endpoints
def drink_list(request):
    """
    Get all the drinks
    serialize them 
    reurn it into JSON format
    """
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many = True)   # all fields
    return JsonResponse(serializer.data)
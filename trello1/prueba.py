from django.views.generic import ListView
from  models import trello1
# Create your views here.
class Trello1List(ListView):
    model=trello1
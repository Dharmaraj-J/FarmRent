from django.forms import ModelForm 
from .models import equipment 
from django.contrib.auth.models import User 
  
  
class EquipementForm(ModelForm): 
     class Meta: 
         model =  equipment 
         fields = ['equipmentname','old'] 
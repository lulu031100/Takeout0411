from django.shortcuts import render

# Create your views here.
# この下追加 hasegawa
from django.views import generic

# Create your views here.

def Index(requests):
    return render(requests, 'takeout/shop_list.html')
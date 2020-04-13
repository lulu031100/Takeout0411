from django.urls import path
from . import views
# このfileは新規作成 hasegawa
app_name = 'takeout'

urlpatterns = [
    path('',views.Index, name='index'), # http://127.0.0.1:8000/takeout/
]
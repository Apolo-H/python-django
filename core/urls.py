from django.urls import path
#foi feito o importe do include acima

#import das views index e contato criadas no core/views
from core.views import  index, product, single

urlpatterns = [
    path('', index),
    path('produtos', product, name='produtos'),
    path('produto/<int:id>/', single , name='single'),
]

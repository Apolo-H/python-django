from django.urls import path
#foi feito o importe do include acima

#import das views index e contato criadas no core/views
from core.views import about, index, product

urlpatterns = [
    path('', index),
    path('product', product),

]

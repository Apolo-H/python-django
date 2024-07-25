from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import  index, product, produto_single,blog, blog_single

#foi feito o importe do include acima

#import das views index e contato criadas no core/views

urlpatterns = [
    path('', index),
    path('produtos', product, name='produtos'),
    path('produtos/<int:id>/', produto_single, name='produto_single'),
    path('blogs', blog, name='blog'),
    path('blog/<slug:slug>/', blog_single, name='blog_single'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

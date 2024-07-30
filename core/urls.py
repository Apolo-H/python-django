from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import  index, product, produto_single,blog, blog_single, about, tec, tec_single
#foi feito o importe do include acima

#import das views index e contato criadas no core/views

urlpatterns = [
    path('', index),
    path('produtos', product, name='produtos'),
    path('produtos/<int:id>/', produto_single, name='produto_s'),
    path('Sobre', about, name='about'),
    path('blogs', blog, name='blog'),
    path('blog/<slug:slug>/', blog_single, name='blog_single'),
    path('tecnologiasingle/<slug:slug>/', tec_single, name='tec_single'),
    path('tecnologias', tec, name='tec'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

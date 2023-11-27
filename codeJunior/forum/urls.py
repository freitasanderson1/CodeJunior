from django.urls import path
from forum.views import ForumIndexView, SecaoView, SubsecaoView, TopicoView, TopicoCreateView, TopicoCreateApiView

from rest_framework.routers import DefaultRouter

app_name= 'forum'

urlpatterns = [
    path('', ForumIndexView.as_view(), name="index-Forum"),
    path('secao/<int:pk>/', SecaoView.as_view(), name="secaoView"),
    path('subsecao/<int:pk>/', SubsecaoView.as_view(), name="subsecaoView"),
    path('topico/<int:pk>/', TopicoView.as_view(), name="topicoView"),
    path('novo-topico/<int:pkSecao>', TopicoCreateView.as_view(), name="topico-create-view"),
    path('novo-topico/<int:pkSecao>/<int:pkSubsecao>/', TopicoCreateView.as_view(), name="topico-create-view2")

    
]

router = DefaultRouter(trailing_slash=False)
router.register(r'api/Topico_Create',TopicoCreateApiView, basename='TopicoApi')

urlpatterns += router.urls
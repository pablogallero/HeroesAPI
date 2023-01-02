from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('heroes/getbyNombre/<str:nombre>/', views.HeroViewSet.as_view({'get': 'getHerobyNombre'}), name='HeroViewSet-getHerobyNombre'),
    path('heroes/modificarHeroe/<int:id>/<str:nombre>/<str:alias>/<int:edad>/<int:altura>/<int:peso>', views.HeroViewSet.as_view({'get': 'modifyHero'}), name='HeroViewSet-modifyHero'),
    path('heroes/anadirHeroe/<str:nombre>/<str:alias>/<int:edad>/<int:altura>/<int:peso>', views.HeroViewSet.as_view({'get': 'addHero'}), name='HeroViewSet-addHero'),
]


# path('heroes/getbyNombre/<str:nombre>/', views.HeroViewSet.as_view({'get': 'getHerobyNombre'}), name='HeroViewSet-getHerobyNombre'),
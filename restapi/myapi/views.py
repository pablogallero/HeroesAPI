from django.shortcuts import render
from rest_framework.decorators import action

# Create your views here.
from rest_framework import viewsets
from django.http import HttpResponse
from django.http import HttpRequest
from rest_framework.response import Response
from .serializers import HeroSerializer
from .models import Hero
from rest_framework import status


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

    @action(detail=False, methods=['get'])
    def getHerobyNombre(self,request,nombre):
        if nombre is not None:
            queryset= self.queryset.filter(name=nombre)
            serializer = HeroSerializer(queryset,many=True)
            return Response(serializer.data )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def modifyHero(self,request,id,nombre,alias,edad,altura,peso):
        idHeroe = id
        if idHeroe is not None:
            queryset= self.queryset.filter(id=idHeroe)
            hero = queryset.get()
            hero.name = nombre
            hero.alias = alias
            hero.edad = edad
            hero.altura = altura
            hero.peso = peso
            hero.save()
            query= self.queryset.filter(id=id)
            serializer = HeroSerializer(query,many=True)
            return Response(serializer.data )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['get'])
    def addHero(self,request,nombre,alias,edad,altura,peso):
        
        if nombre is not None:
            
            queryset= self.queryset.filter(name=nombre)
            if len(queryset) == 0:
                hero = Hero(name = nombre,alias = alias,edad = edad,altura = altura,peso = peso)
                hero.save()
                
                return Response(True)
            else:
                return Response(status=status.HTTP_409_CONFLICT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
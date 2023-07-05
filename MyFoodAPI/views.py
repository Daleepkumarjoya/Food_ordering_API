from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from .myPagination import MyPageNumberPagination
from .serializers import HomeModelSerializer, AboutModelSerializer, OrderModelSerializer, contacModelSerializer, \
    MenuModelSerializer
from .throttling import DKThrottle
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import viewsets
from .models import HomeModel, AboutModel, OrderModel, contacModel, MenuModel
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from .throttling import DKThrottle

# Create your views here.


class HomeModelViewSet(viewsets.ModelViewSet):
    queryset = HomeModel.objects.all()
    serializer_class = HomeModelSerializer
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'HomeView'
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['name']
    Search_fields = ['name']
    pagination_class = MyPageNumberPagination


class AboutModelViewSet(viewsets.ModelViewSet):
    queryset = AboutModel.objects.all()
    serializer_class = AboutModelSerializer
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'HomeView'


class MenuModelViewSet(viewsets.ModelViewSet):
    queryset = MenuModel.objects.all()
    serializer_class = MenuModelSerializer
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'HomeView'
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['name']
    Search_fields = ['name']
    pagination_class = MyPageNumberPagination


class contacModelViewSet(viewsets.ModelViewSet):
    queryset = contacModel.objects.all()
    serializer_class = contacModelSerializer
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, DKThrottle]
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['name']
    Search_fields = ['name']
    pagination_class = MyPageNumberPagination


class OrderModelViewSet(viewsets.ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = OrderModelSerializer
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, DKThrottle]
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['name']
    Search_fields = ['name']
    pagination_class = MyPageNumberPagination

from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'PageNumber'
    # page_size_query_param = 'Records'
    # max_page_size = 3
    ordering = ['name']



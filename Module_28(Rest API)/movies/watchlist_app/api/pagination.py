from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class MoviePageNumberPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'pg'

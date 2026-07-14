from rest_framework.pagination import PageNumberPagination


#Custorm pagination to display 10 data:
class PaginationOfTen(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
  
  
#Custorm pagination to display 20 data:  
class PaginationOfTwenty(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100
    

#Custorm pagination to display 50 data:
class PaginationOfFifty(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100
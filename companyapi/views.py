from django.http import HttpResponse
def home_page(request):
    print("'requested home page: '")
    return HttpResponse("This is the home page:")

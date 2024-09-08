from django.urls import path
from django.http import HttpResponse

def first_view(request):
    html = """
    <html>
    <body>
    <h1>My First View</h1><hr>
    </body>
    </html>
    """
    
    return HttpResponse(html)

urlpatterns = [
    path("one", first_view, name="view_one"),
    path("two", first_view, name="view_two")
]

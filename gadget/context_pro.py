from .models import Category, Tag

def view_all(request):
    context = {
        'categories':Category.objects.all()
    }
    return context
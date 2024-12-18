from django.shortcuts import render

from catalog.models import Book,Author,BookInstance,Genre

def index(request):


    num_books = Book.objects.all().count() #책 오브젝트를 모두 가져오고 갯수를 카운트
    num_instances = BookInstance.objects.all().count()



    num_instances_available = BookInstance.objects.filter(status__exact='a').count()


    num_authors = Author.objects.count()

    
    context = {
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instances_available':num_instances_available,
        'num_authors' : num_authors,
    }


    return render(request,'index.html',context=context)

from django.views import generic


class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book
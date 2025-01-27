from django.contrib import admin

# Register your models here.


from catalog.models import Author,Genre,Book,BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','borrower','due_back','id')
    list_filter = ('status','due_back')


    fieldsets = (
        (None, {
            'fields' : ('book','imprint','id')
        }),
        ('Avalability', {
            'fields' : ('status','due_back','borrower')
        }),
    )

from django.db import models

# Create your models here.

class Genre(models.Model): #책의 장르를 정하는 모델
    name = models.CharField(max_length=200,help_text='Enter a book genre(e.g. Science Fiction)')

    #genre string 처리
    def __str__(self): #자기 이름을 반환하는 함수
        return self.name
    
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200) #책 제목

    #foreign키를 사용해준다. 작가는 여러명이 될 수 있어서
    author = models.ForeignKey('Author',on_delete=models.SET_NULL, null=True) #작가이름

    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book") #줄거리 

    #isbn ,책 보관을 위한 고유번호
    isbn = models.CharField('ISBN',max_length=13,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number </a>')

    #ManyToManyField를 사용해서 장르가 여러 book들을 포함할 수 있게 한다.
    genre = models.ManyToManyField(Genre,help_text='Select a genre for this book')


    #book string 처리
    def __str__(self):
        return self.title
    
    # book 레코드에 접근할 수 있는 url를 return
    def get_absolute_url(self):
        return reverse('book-detail',args=[str(self.id)])
    

import uuid


class BookInstance(models.Model): #책을 빌려가면 책의 복사본
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, help_text='Unique whole library')
    book = models.ForeignKey('Book',on_delete=models.SET_NULL,null=True)
    imprint = models.CharField(max_length=200) #출판사
    due_back = models.DateField(null=True,blank=True) #언제 돌려받을지

    LOAN_STATUS = ( #대출상태
    ('m','Maintenance'),
    ('o','On loan'),
    ('a','Available'),
    ('r','Reserved'),
    )
    status = models.CharField(#책의 정보
    max_length=1,
    choices=LOAN_STATUS,
    blank=True,
    default='m',
    help_text='Book availability',
    )


    #메타 데이터로 반납일자 사용
    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'
    
class Author(models.Model): #작가모델
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)
    date_of_death = models.DateField('Died',null=True,blank=True)

    #메타 데이터 이름을 사용
    class Meta:
        ordering = ['last_name','first_name']
    
    def get_absolute_url(self):
        return reverse('author-detail',args=[str(self.id)])
    
    def __str__(self):
        return f'{self.last_name},{self.first_name}'
from .models import Books

class BookAlreadyExistError(Exception):
    pass 

class BookNotExistError(Exception):
    pass 

def getBooks():
    return list(Books.objects.values_list('title', flat=True))

def addBook(new_title,new_description):
    if Books.objects.filter(title=new_title).exists():
        raise BookAlreadyExistError("Book with the same title already exist")
    new_book = Books(title=new_title, description=new_description)
    new_book.save()
    return new_book.Id

def updateBook(oldTitle, newTitle, newDescription):
    if not Books.objects.filter(title=oldTitle).exists():
        raise BookNotExistError("Book not found")
    matching_book = Books.objects.filter(title=oldTitle)[0]
    if newTitle != "":
        matching_book.title=newTitle
    if newDescription!="":
        matching_book.description=newDescription
    matching_book.save()
    return True
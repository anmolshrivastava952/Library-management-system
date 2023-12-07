
from multiprocessing import AuthenticationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import django
django.setup()
from . import app
from . import token

@ swagger_auto_schema(method='Get',
    responses={
        200: openapi.Response(
            description='Success',
            schema=openapi.Schema(
                type='object',
                properties={
                    'ListOfBooks': openapi.Schema(type='array',items=openapi.Schema(type='string'))
                }
            )
        ),
        400: openapi.Response(
            description='Bad Request',
            schema=openapi.Schema(
                type='object',
                properties={
                    'error': openapi.Schema(type='string')
                }
            )
        ),
        500: openapi.Response(
            description='Internal Server Error',
            schema=openapi.Schema(
                type='object',
                properties={
                    'error': openapi.Schema(type='string')
                }
            )
        )
    }
)
@api_view(['Get'])
def getBookDetails(request):
    # Serialize the queryset to JSON
    try:
        return Response({'ListOfBooks':app.getBooks()})
    except Exception as e:
        return Response({"error":"Unknown error occurred while retrieving"})


@ swagger_auto_schema(method='post', request_body=openapi.Schema(
    type='object',
    required=['username','password'],
    properties={
        'username':openapi.Schema(type='string'),
        'password':openapi.Schema(type='string')
    }
),
    responses={
        200: openapi.Response(
            description='Success',
            schema=openapi.Schema(
                type='object',
                properties={
                    'jwt': openapi.Schema(type='string')
                })
        ),
        400: openapi.Response(
            description='Bad Request',
            schema=openapi.Schema(
                type='object',
                properties={
                    'error': openapi.Schema(type='string')
                }
            )
        ),
        500: openapi.Response(
            description='Internal Server Error',
            schema=openapi.Schema(
                type='object',
                properties={
                    'error': openapi.Schema(type='string')
                }
            )
        )
    }
)
@api_view(['post'])
def adminLogin(request):
    try:
        userName=request.data['username']
        password=request.data['password']
        if((userName!='admin') or (password!='AnmolShriv')):
            raise AuthenticationError("username and password don't match")
        else:
            return Response({"jwt": token.generatejwt()})
    except AuthenticationError as e:
        return Response({"error":e})


@ swagger_auto_schema(method='post', request_body=openapi.Schema(
    type='object',
    required=['jwt','username','title','description'],
    properties={
        'jwt': openapi.Schema(type='string'),
        'username':openapi.Schema(type='string'),
        'title':openapi.Schema(type='string'),
        'description':openapi.Schema(type='string')
    }
),
responses={
        200: openapi.Response(
            description='Success',
            schema=openapi.Schema(
                type='object',
                properties={
                    'id': openapi.Schema(type='integer')
                })
        ),
        400: openapi.Response(
            description='Bad Request',
            schema=openapi.Schema(
                type='object',
                properties={
                    'error': openapi.Schema(type='string')
                }
            )
        ),
        500: openapi.Response(
            description='Internal Server Error',
            schema=openapi.Schema(
                type='object',
                properties={
                    'error': openapi.Schema(type='string')
                }
            )
        )
    }
)
@api_view(['post'])
def addBookRequest(request):
    
    try:
        Jtoken = request.data['jwt']
    except Exception as e:
        return Response({"error":"no token present"})
    
    try:
        username=request.data['username']
    except Exception as e:
        return Response({"error":"no username is provided"})
    
    try:
        if(not token.verifyjwt(username, Jtoken)):
            raise AuthenticationError("Invalid credentials")
    except Exception as e:
        return Response({"error":"invalid credentials"})
    
    
    try:
        title=request.data['title']
    except Exception as e:
        return Response({"error":"no title provided"})
    try:
        description=request.data['description']
    except Exception as e:
        return Response({"error":"no description provided"})
    try:
        return Response({"id":app.addBook(title,description)})
    except Exception as e:
        return Response({"error":"book already exist"})
    

@ swagger_auto_schema(method='put', request_body=openapi.Schema(
    type='object',
    required=['username','jwt','old_title'],
    properties={
        'username':openapi.Schema(type='string'),
        'jwt':openapi.Schema(type='string'),
        'oldTitle':openapi.Schema(type='string'),
        'newTitle':openapi.Schema(type='string'),
        'newDescription':openapi.Schema(type='string')
    }
),
    responses={
        200: openapi.Response(
            description='Success',
            schema=openapi.Schema(
                type='object',
                properties={
                    'Update': openapi.Schema(type='string')
                })
        ),
        400: openapi.Response(
            description='Bad Request',
            schema=openapi.Schema(
                type='object',
                properties={
                    'error': openapi.Schema(type='string')
                }
            )
        ),
        500: openapi.Response(
            description='Internal Server Error',
            schema=openapi.Schema(
                type='object',
                properties={
                    'error': openapi.Schema(type='string')
                }
            )
        )
    }
)
@api_view(['put'])
def UpdateBookRequest(request):
    try:
        Jtoken = request.data['jwt']
    except Exception as e:
        return Response({"error":"no token present"})
    try:
        username=request.data['username']
    except Exception as e:
        return Response({"error":"no username is provided"})
    
    try:
        if(not token.verifyjwt(username, Jtoken)):
            raise AuthenticationError("Invalid credentials")
    except Exception as e:
        return Response({"error":"invalid credentials"})
    try:
        oldTitle=request.data['oldTitle']
    except Exception as e:
        return Response({"error":"no book is provided for change"})
    try:
        newTitle=''
        newDescription=''
        if 'newTitle' in request.data:
            newTitle=request.data['newTitle']
        if 'newDescription' in request.data:
            newDescription=request.data['newDescription']
        if newTitle=='' and newDescription=='':
            raise Exception("no change to make")
    except Exception as e:
        return Response({"error":"no change to be made"})
    
    try:
        return Response({"Update":app.updateBook(oldTitle,newTitle,newDescription)})
    except Exception as e:
        return Response({"Book does not exist"})
    



    
    



from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ForumSerializer
from forum.models import Post

# view api

#create api view
@api_view(['POST',])
def createpost(request):
    post = Post()
    if request.method=='POST':
        serializer = ForumSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# forum update api
@api_view(['PUT',])
def forumupdate(request,id):
    try:
        post = Post.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        serializer = ForumSerializer(post,data=request.data)
        data = []
        if serializer.is_valid():
            serializer.save()
            data['success']="update success"
        return Response(data=data)


#fourm delete api
@api_view(['DELETE',])
def forumdelete(request,id):
    try:
        post = Post.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        data = {}
        if post.delete():
            data['success']="Succesfully Deleted";
        else:
            data['error']="sorry error occured";
        return Response(data=data)

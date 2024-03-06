from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import NoteSerializer
from .models import Note
@api_view(['GET'])
def getRoutes(request):
    routes=[
        {
            'Endpoint':'/notes/',
            'method':'GET',
            'body':'None',
            'descreption':'Returns an array of notes',
        },
        {
            'Endpoint':'/notes/id',
            'method':'GET',
            'body':'None',
            'descreption':'Returns single note object',
        }
    ]
    return Response(routes)

#get all notes
@api_view(['GET'])
def getNotes(request):
    notes=Note.objects.all()
    serializer=NoteSerializer(notes,many=True)
    return Response(serializer.data)

#get single note
@api_view(['GET'])
def getNote(request,pk):
    note=Note.objects.get(id=pk)
    serializer=NoteSerializer(note,many=False)
    return Response(serializer.data)
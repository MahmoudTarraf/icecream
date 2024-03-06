from rest_framework.serializers import ModelSerializer
from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note  # Replace 'Note' with your actual model name
        fields = '__all__'  # Or specify the fields you want to include
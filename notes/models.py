from django.db import models

class Note(models.Model):
    TEXT = 'text'
    AUDIO = 'audio'
    VIDEO = 'video'
    NOTE_TYPES = [
        (TEXT, 'Text'),
        (AUDIO, 'Audio'),
        (VIDEO, 'Video'),
    ]

    content = models.TextField()
    type = models.CharField(max_length=5, choices=NOTE_TYPES)

    def __str__(self):
        return f'Note {self.id}'

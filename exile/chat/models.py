from django_mongoengine import Document, EmbeddedDocument, fields
from django.utils.six import python_2_unicode_compatible
from channels import Group
from .settings import MSG_TYPE_MESSAGE
from django_mongoengine import Document, EmbeddedDocument, fields
from bson import ObjectId
import json
import datetime

@python_2_unicode_compatible
class Miembro(Document):
    created_at = fields.DateTimeField(
        default=datetime.datetime.now, editable=False,
    )
    usuario = fields.IntField(unique=True)
    nombre = fields.StringField()
    apellidos = fields.StringField()
    username = fields.StringField()
    cuenta = fields.IntField(blank=True, null=True)

    def __str__(self):
        return u"%s %s id: %d" % (self.nombre, self.apellidos, self.usuario)
# end class

@python_2_unicode_compatible
class Room(Document):
    nombre = fields.StringField(blank=True, null=True)
    grupo = fields.BooleanField(default=False)
    miembros = fields.ListField(fields.ReferenceField(Miembro))

    def __unicode__(self):
        return self.nombre or ''
    # end def

    def __str__(self):
        return self.nombre or ''

    @property
    def websocket_group(self):
        """
        Returns the Channels Group that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return Group("room-%s" % self.id)

    def send_message(self, message, user, msg_type=MSG_TYPE_MESSAGE):
        """
        Called to send a message to the room on behalf of a user.
        """
        final_msg = {'room': str(self.id), 'message': message, 'username': user.username, 'msg_type': msg_type}
        miembro = Miembro.objects(usuario=user.pk).first()
        mensaje = Mensaje(mensaje=message, emisor=miembro, room=self)
        mensaje.save()
        # Send out the message to everyone in the room
        self.websocket_group.send(
            {"text": json.dumps(final_msg)}
        )


@python_2_unicode_compatible
class Mensaje(Document):
    mensaje = fields.StringField()
    emisor = fields.ReferenceField(Miembro)
    room = fields.ReferenceField(Room)
    leido = fields.BooleanField(default=False)
    recibido = fields.BooleanField(default=True)

    def __str__(self):
        return u"%s" % (self.mensaje)

    def __unicode__(self):
        return u"%s" % (self.mensaje)

class Notificacion(Document):
    miembro = fields.ReferenceField(Miembro)
    mensaje = fields.StringField()
    created_at = fields.DateTimeField(
        default=datetime.datetime.now, editable=False,
    )
    leido = fields.BooleanField(default=False)
# end class
"""
import json
from django.db import models
from django.utils.six import python_2_unicode_compatible
from channels import Group

from .settings import MSG_TYPE_MESSAGE


@python_2_unicode_compatible
class Room(models.Model):

    # A room for people to chat in.


    # Room title
    title = models.CharField(max_length=255)

    # If only "staff" users are allowed (is_staff on django's User)
    BooleanField = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def websocket_group(self):

        # Returns the Channels Group that sockets should subscribe to to get sent
        # messages as they are generated.

        return Group("room-%s" % self.id)

    def send_message(self, message, user, msg_type=MSG_TYPE_MESSAGE):

        # Called to send a message to the room on behalf of a user.

        final_msg = {'room': str(self.id), 'message': message, 'username': user.username, 'msg_type': msg_type}

        # Send out the message to everyone in the room
        self.websocket_group.send(
            {"text": json.dumps(final_msg)}
        )
"""

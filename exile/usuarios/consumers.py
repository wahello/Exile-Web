import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
from subcripcion.models import Cuenta
from django.db.models import Q
from channels.generic.websockets import WebsocketDemultiplexer, JsonWebsocketConsumer
import biding


@channel_session_user_from_http
def ws_connect(message):
    message.reply_channel.send({"accept": True})
    if message.user:
        cuenta = Cuenta.objects.filter(
            Q(cliente=message.user.pk) | Q(usuario=message.user.pk)).first()
        if cuenta:
            Group('noti-%d' % cuenta.id).add(message.reply_channel)
            Group('noti-%d' % cuenta.id).send({
                'text': json.dumps({
                    'username': message.user.username,
                    'is_logged_in': True
                })
            })


@channel_session_user
def ws_disconnect(message):
    if message.user:
        cuenta = Cuenta.objects.filter(
            Q(cliente=message.user.pk) | Q(usuario=message.user.pk)).first()
        if cuenta:
            Group('noti-%d' % cuenta.id).send({
                'text': json.dumps({
                    'username': message.user.username,
                    'is_logged_in': False
                })
            })
            Group('noti-%d' % cuenta.id).discard(message.reply_channel)


class EchoConsumer(JsonWebsocketConsumer):
    http_user = True

    def connection_groups(self, **kwargs):
        if kwargs["pk"] is not 0 or not None:
            return ['noti-%s' % kwargs["pk"]]
        # end if
        return ['noti-0']
    # end def

    def connect(self, message, multiplexer, **kwargs):
        # Send data with the multiplexer
        if kwargs["pk"] is not 0 or not None:
            Group('noti-%s' % kwargs["pk"]).send({
                'text': json.dumps({
                    'username': message.user.username,
                    'is_logged_in': True
                })
            })
        # multiplexer.send({"status": "I just connected!"})

    def disconnect(self, message, multiplexer, **kwargs):
        print("Stream %s is closed" % multiplexer.stream)
        if kwargs["pk"] is not 0 or not None:
            Group('noti-%s' % kwargs["pk"]).send({
                'text': json.dumps({
                    'username': message.user.username,
                    'is_logged_in': False
                })
            })

    def receive(self, content, multiplexer, **kwargs):
        # Simple echo
        multiplexer.send({"original_message": content})


class AnotherConsumer(JsonWebsocketConsumer):
    def receive(self, content, multiplexer=None, **kwargs):
        # Some other actions here
        pass

    def connect(self, message, multiplexer, **kwargs):
        # Send data with the multiplexer
        message.reply_channel.send({"accept": True})
        multiplexer.send({"status": "I just connected!2"})


class Demultiplexer(WebsocketDemultiplexer):

    # Wire your JSON consumers here: {stream_name : consumer}
    consumers = {
        "echo": EchoConsumer,
        # "other": AnotherConsumer,
    }

"""
    Biding
"""


class DemultiplexerBiding(WebsocketDemultiplexer):

    consumers = {
        "cargo": biding.CargoValueBinding.consumer,
        "empleado": biding.EmpleadoValueBinding.consumer,
        "asistente": biding.AsistenteValueBinding.consumer,
        "grupo": biding.GrupoValueBinding.consumer
    }

    def connection_groups(self, **kwargs):
        return ["noti-%s" % kwargs["pk"]]
    # end def
# end class

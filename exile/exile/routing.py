from channels.routing import route, route_class
from usuarios.consumers import ws_connect, ws_disconnect, Demultiplexer, DemultiplexerBiding


channel_routing = [
    # route('websocket.connect', ws_connect),
    # route('websocket.disconnect', ws_disconnect),
    route_class(Demultiplexer, path="^/test/(?P<pk>\d+)/"),
    # route_class(DemultiplexerBiding, path="^/biding/(?P<pk>\d+)/")
]

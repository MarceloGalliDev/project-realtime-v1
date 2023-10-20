from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<nome_sala>\w+)/$", consumers.ChatConsumer.as_asgi()),
]

# vamos fazer um re-path pois vamos utilizar expressões regulares
# consumer faz a ponte entre navegador e aplicação

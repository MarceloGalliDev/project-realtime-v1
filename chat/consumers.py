from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):
    # conectando na sala
    async def connect(self):
        # recuperando nome da sala
        self.room_name = self.scope['url_route']['kwargs']['nome_sala']
        self.room_group_name = f'chat_{self.room_name}'

        # entrando na sala
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

    # saindo da sala
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    # recebendo mensagem do websocket
    # text_data é os dados que estamos recebendo
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        mensagem = text_data_json['mensagem']

        # enviando a mensagem para a sala
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': mensagem
            }
        )

    # recebendo mensagem da sala
    async def chat_message(self, event):
        mensagem = event['message']

        # envia a mensagem para o websocket
        await self.send(text_data=json.dumps({
            'mensagem': mensagem
        }))

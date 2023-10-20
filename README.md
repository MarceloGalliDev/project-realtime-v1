# Project-realtime-v1

### Instalando bibliotecas
> pip install django

> pip install django-channels

> pip install bootstrap4

> pip install -U 'channels[daphne]'

> pip install channels-redis


### Configurações settings.py
>```
> INSTALLED_APPS = [
>   'daphne',
>   'bootstrap4',
> ]
>```

>```
> ASGI_APPLICATION = 'realtime.asgi.application'
> CHANNEL_LAYERS = {
>     "default": {
>         "BACKEND": "channels_redis.core.RedisChannelLayer",
>         "CONFIG": {
>             "hosts": [("localhost", 6379)],
>        },
>     },
> }
>```


### Explicação
Colocamos o redis como controle dos channels.
Consumer faz a ponte entre navegador e aplicação.

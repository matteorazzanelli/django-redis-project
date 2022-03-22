from django.apps import AppConfig
# import redis

class BachecaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bacheca'
    def ready(self):
        # print('Hello world!')
        # client = redis.StrictRedis(host='127.0.0.1', port=6379, password='',db=0)
        # client.set('nome','Augusto')
        # print(client.get('nome'))
        pass


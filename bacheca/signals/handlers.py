import redis
client = redis.StrictRedis(host='127.0.0.1', port=6379, password='',db=0)


from django.contrib import messages
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from ..utils import get_ip_address

"""
  check whether or not the ip is changed
"""
@receiver(user_logged_in)
def logged_in_message(sender, user, request, **kwargs):
  current_user_ip = get_ip_address(request)
  # if user does not exist set it up
  if not client.exists(str(user)):
    client.set(str(user),current_user_ip)
  else:
    if client.get(str(user)).decode('utf-8') != current_user_ip:
      messages.warning(request, "IP has changed")
    else:
      messages.info(request, "Welcome back %s" %user)

user_logged_in.connect(logged_in_message) # take an action when login
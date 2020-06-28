import random
import string
'''
Obselete code generator method
def code_generator(size=6,chars='abcdefghijklmnopqrstuvwzyz'):
    return ''.join(random.choice(chars)for _ in range(size))
'''

def code_generator(size=6,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars)for _ in range(size))


def create_shortcode(instance,size=6):
    new_code=code_generator(size=size)
    KirrUrl=instance._class_

    code_exists=KirrUrl.objects.filter(shortcode=new_code).exists()
    if(code_exists):
        return create_shortcode(size=size)
    return new_code

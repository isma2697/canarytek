from django.conf import LazySettings
from django.contrib.auth.models import User, Group, Permission

def _create_user(user_identify):
    print(user_identify)

    # Obtener el valor de GROUP_CREATE, por defecto es False
    GROUP_CREATE = settings.SAML2_AUTH.get('GROUP_CREATE', False)

    # Obtener el nombre de usuario y los grupos
    email = user_identify['emailAddress']
    group_names = user_identify['group']

    # Crear el usuario si no existe
    user, created = User.objects.get_or_create(email=email)

    if GROUP_CREATE:

        # Para cada nombre de grupo, buscar el grupo existente o crear uno nuevo
        for group_name in group_names:
            try:
                #Busca el grupo por el nombre
                group = Group.objects.get(name=group_name)

            #Si el grupo no existe
            except Group.DoesNotExist:

                #Crea el grupo
                group = Group.objects.create(name=group_name)

            # Agregar el usuario al grupo
            group.user_set.add(user)
    else:

        # Si GROUP_CREATE es False, buscar el primer grupo existente en la lista y agregar el usuario a ese grupo
        for group_name in group_names:
            try:
                #Busca el grupo por el nombre
                group = Group.objects.get(name=group_name)

                # Agregar el usuario al grupo
                group.user_set.add(user)

                break

            #Si el grupo no existe
            except Group.DoesNotExist:
                pass

    return user

settings = LazySettings()

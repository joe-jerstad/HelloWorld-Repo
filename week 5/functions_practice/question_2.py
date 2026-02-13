def access_rights(user_role):
    user_role = user_role.lower()

    if user_role == 'user':
        return 'limited'
    elif user_role == 'admin':
        return 'full'
    elif user_role == 'guest':
        return 'view'
def is_valid_user(user):
    keys = ['email']
    return all(key in user for key in keys)

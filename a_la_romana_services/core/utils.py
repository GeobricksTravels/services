def is_valid_user(user):
    keys = ['user_id', 'name', 'email', 'image_url']
    return all(key in user for key in keys)

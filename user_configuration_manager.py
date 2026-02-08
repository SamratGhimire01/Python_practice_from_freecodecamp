test_settings={'Theme':'dark','Notifications':'enabled','Volume':'high'}

def add_setting(dic,tup):
    key,value=tup
    key=key.lower()
    value=value.lower()
    
    if key in dic:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    dic[key]=value
    return f"Setting '{key}' added with value '{value}' successfully!"
        
print(add_setting({'theme': 'light'}, ('THEME', 'dark')))


def update_setting(dic,tup):
    key,value=tup
    key=key.lower()
    value=value.lower()
    if not key in dic:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    dic[key]=value
    return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(dic,tup):
    key=tup
    key=key.lower()
    if not key in dic:
        return "Setting not found!"
    del dic[key]
    return f"Setting '{key}' deleted successfully!"

def view_settings(dic):
    if not dic:
        return "No settings available."
    result="Current User Settings:\n"
    for key,value in dic.items():
        key=key.capitalize()
        result += f"{key}: {value}\n"
    return result
    
print(view_settings(test_settings))
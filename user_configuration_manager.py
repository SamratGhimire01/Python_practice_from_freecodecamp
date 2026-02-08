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


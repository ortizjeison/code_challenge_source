#Set local_run = True for local development
#Set local_run = False for running in Cloud Run Functions

local_run = False

def local():
    if local_run:
        return True
    else:
        return False
    
def base_path():
    if local_run:
        return ''
    else:
        return '/'
from platform import system as getos

def check_path(unixpath: str):
    if getos() == "windows":
        return unixpath.replace('/', '\\')
    else:
        return unixpath

def write_once(path: str, con: str):
    a = open(path, 'w')
    a.write(con)
    a.close()

def read_once(path: str):
    a = open(path, 'r')
    b = a.read()
    a.close()
    return b
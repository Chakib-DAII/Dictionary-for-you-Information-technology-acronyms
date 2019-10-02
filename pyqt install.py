import pip
#stackOverFlow
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])
        
try:
    import PyQt5
    print("already installed!!")
except:
    install('pyqt5')
    import PyQt5
    print("done, installed!!")
    

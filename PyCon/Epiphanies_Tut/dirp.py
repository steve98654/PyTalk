def _dir(obj='__secret', _CLUTTER=dir()): 
    """ 
    A version of dir that excludes clutter and private names. 
    """ 
    if obj == '__secret': 
        names = globals().keys() 
    else: 
        names = dir(obj) 
    return [n for n in names if n not in _CLUTTER and not n.startswith
('_')] 
     
def _dirn(_CLUTTER=dir()): 
    """ 
    Display the current global namespace, ignoring old names. 
    """ 
    return dict([ 
        (n, v) for (n, v) in globals().items() 
        if not n in _CLUTTER and not n.startswith('_')]) 
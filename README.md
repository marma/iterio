# IterIO

Create file-like objects from iterables (of bytes-like objects)

## Usage

    from iterio import open
    
    >>> i = open([ b'123', b'456', b'789' ])
    >>> r.read(4)
    '1234'
    
    >>> i = open([ b'123', b'456', b'789' ], mode='rb')
    >>> i.read(5)
    b'12345'

    

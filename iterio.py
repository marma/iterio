from io import RawIOBase

class IterIO(RawIOBase):
    def __init__(self, i):
        self.it = i
        self.current = next(i)
        self.n = 0

    
    def read(self, n=-1):
        self._assertOpen()

        if self.current == None:
            return b''

        if n == -1:
            return self.readall()

        b = None
        ret = []
        while n > 0 and b != b'':
            if self.n == len(self.current):
                try:
                    self.current = next(self.it)
                    self.n = 0
                except StopIteration:
                    break

            b = self.current[self.n : self.n + min(n, len(self.current) - self.n) ]
            self.n += len(b)
            n -= len(b)
            ret += [ b ]

        return b''.join(ret)


    def readable(self):
        return True


    def readall(self):
        self._assertOpen()

        ret = b''.join([ self.current[self.n:len(self.current)] ] + [ x for x in self.it ])
        self.current = None
        self.n = 0
        
        return ret


    def seek(self, n, whence):
        self._assertOpen()

        raise Exception('Stream not seekable')


    def seekable(self):
        return False


    def writable(self):
        return False


    def _assertOpen(self):
        if self.closed:
            raise ValueError('I/O operation on closed stream')

    

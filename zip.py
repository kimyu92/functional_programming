class Zip:
    def __init__(self, *args):
        self.iterate = [iter(a) for a in args]
        
    def __iter__(self):
        return Zip.iterator(self)
        
    class iterator:
        def __init__(self, zip):
            self.iterate = zip.iterate
            
        def __next__(self):
            return tuple([next(v) for v in self.iterate])
        
        def __iter__(self):
            return self
            

x = iter(Zip([1,2],[5,6]))
print(next(x))
print(next(x))


def myzip(*args):
    iterates = [iter(it) for it in args]
    try:
        while True:
            yield tuple([next(v) for v in iterates])
    except StopIteration:
        pass
    
    
y = iter(myzip([2,3],[5,3]))
print(next(y))
print(next(y))


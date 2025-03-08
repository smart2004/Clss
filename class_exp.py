class Exp: 
    '''Exp class.''' 
 
    def func(self): 
        '''func method.''' 
        self.a = 5 
        self.b = 'win'  

class Int:

    e = Exp() 
    e.func() 

    print(e.a, e.b)
    print(e.__dict__)

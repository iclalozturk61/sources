class Book():
    favs = []

    def __init__(self, title, author, available): 
        self.title = title
        self.author = author    
        self.available = available
        
    def __str__(self):
        return f"{self.title} by {self.author}, Available: {self.available}"
    
    __hash__ = None

    def __repr__(self):#__repr__ → Nesnenin geliştiriciye yönelik string temsili. Bu kodda ikisinin sonucu aynı tutulmuş
        return self.__str__()
    
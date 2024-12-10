class Node:
    def __init__(self, init_data: object):
        self.data = init_data
        self.next = None
        
    def get_data(self) -> object:
        return self.data
    
    def get_next(self) -> object:
        return self.next
    
    def set_data(self, new_data: object) -> None:
        self.data = new_data
        
    def set_next(self, new_next: object) -> None:
        self.next = new_next
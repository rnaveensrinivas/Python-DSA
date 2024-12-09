from random import randrange

class Task:
    def __init__(self, print_request_time: int):
        """print_request_time: the time at which this task was requested"""
        self.print_request_time = print_request_time
        self.number_of_pages_to_print = randrange(1,21)
        
    def get_stamp(self) -> int:
        return self.print_request_time
    
    def get_number_of_pages_to_print(self) -> int:
        return self.number_of_pages_to_print
    
    def get_waiting_time(self, printer_assigned_time: int) -> int:
        return printer_assigned_time - self.print_request_time
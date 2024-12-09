import Task

class Printer:
    def __init__(self, pages_per_minute):
        self.pages_per_minute = pages_per_minute # eg 20 pages/minute
        self.current_task = None # task object
        self.time_remaining = 0 # in seconds
    
    def tick(self) -> None:
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None
    
    def is_free(self) -> bool:
        return self.current_task == None
    
    def start_next(self, new_task: Task) -> None:
        self.current_task = new_task
        self.time_remaining = (new_task.get_number_of_pages_to_print() /
                               self.pages_per_minute) * 60
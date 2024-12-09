import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Printer
import Task
import Queue
import random


def new_print_task(number_of_students_per_hour: int, 
                   number_of_tasks_per_student: int) -> int:
    """
    Consider 10 students in lab for any given hour. 
    Each student uses the printer twice in an hour. 
    Hence, printer gets 20 tasks per hour. 
    20 tasks/hr => a task every 3 minutes. 
    3 minutes = 180 seconds. 
    
    Note we don't know when a student will give print request,
    it could be back to back or evenly distributed across the hour.
    Hence we use random to simulate it. 
    """
    
    tasks_per_hour = number_of_students_per_hour * number_of_tasks_per_student
    MINUTES_IN_HOUR = 60
    task_every_minutes = MINUTES_IN_HOUR // tasks_per_hour   
    task_every_seconds = task_every_minutes * 60 
    return random.randrange(1,task_every_seconds+1) == task_every_seconds

def simulation(time_frame_in_seconds: int, 
               pages_per_minute: int, 
               number_of_students_per_hour: int = 10,
               number_of_tasks_per_student: int = 2,
               students_can_wait: bool = False) -> None:
    
    lab_printer = Printer.Printer(pages_per_minute)
    print_queue = Queue.Queue()
    waiting_time = []
    
    for current_second in range(time_frame_in_seconds):
        
        if new_print_task(number_of_students_per_hour,
                          number_of_tasks_per_student):
            task = Task.Task(current_second)
            print_queue.enqueue(task)
            
        if lab_printer.is_free() and not print_queue.is_empty():
            next_task = print_queue.dequeue()
            waiting_time.append(next_task.get_waiting_time(current_second))
            lab_printer.start_next(next_task)
            
        lab_printer.tick()
        
    if students_can_wait:
        while not print_queue.is_empty():
            if lab_printer.is_free():
                next_task = print_queue.dequeue()
                waiting_time.append(next_task.get_waiting_time(current_second))
                lab_printer.start_next(next_task)
            lab_printer.tick()
            current_second += 1
        
    if len(waiting_time) > 0:
        average_wait = sum(waiting_time) / len(waiting_time)
        print("Average wait %6.2f secs %3d tasks remaining"%(average_wait, 
                                                             print_queue.size()))
    else:
        print("No tasks were created in the given time frame.")
          
print("For print per minute of 5:")  
for _  in range(10):
    simulation(time_frame_in_seconds=3600, 
               pages_per_minute=5, 
               number_of_students_per_hour=15,
               number_of_tasks_per_student=3,
               students_can_wait=False)
    
print("\nFor print per minute of 10:")  
for _  in range(10):
    simulation(time_frame_in_seconds=3600, 
               pages_per_minute=10, 
               number_of_students_per_hour=15,
               number_of_tasks_per_student=3,
               students_can_wait=False)

print("\n\nFor print per minute of 5 and students can wait:")  
for _  in range(10):
    simulation(time_frame_in_seconds=3600, 
               pages_per_minute=5, 
               number_of_students_per_hour=10,
               number_of_tasks_per_student=2,
               students_can_wait=True)
    
print("\nFor print per minute of 10 and students can wait:")  
for _  in range(10):
    simulation(time_frame_in_seconds=3600, 
               pages_per_minute=10, 
               number_of_students_per_hour=10,
               number_of_tasks_per_student=2,
               students_can_wait=True)
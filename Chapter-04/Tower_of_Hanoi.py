def move_tower(height: int, 
               from_pole: str, 
               to_pole: str, 
               with_pole: str) -> None:
    if height >= 1:
        # leaving the last disk
        move_tower(height-1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height-1, with_pole, to_pole, from_pole)

def move_disk(from_pole: str, 
              to_pole: str)-> None:
    print(f"Moving Disk from {from_pole} to {to_pole}")
    
move_tower(1, "Start Tower", "End Tower", "Intermediate Tower")
print()
move_tower(2, "Start Tower", "End Tower", "Intermediate Tower")
print()
move_tower(3, "Start Tower", "End Tower", "Intermediate Tower")
print()
move_tower(4, "Start Tower", "End Tower", "Intermediate Tower")
print()

_ = """
Moving Disk from Start Tower to End Tower

Moving Disk from Start Tower to Intermediate Tower
Moving Disk from Start Tower to End Tower
Moving Disk from Intermediate Tower to End Tower

Moving Disk from Start Tower to End Tower
Moving Disk from Start Tower to Intermediate Tower
Moving Disk from End Tower to Intermediate Tower
Moving Disk from Start Tower to End Tower
Moving Disk from Intermediate Tower to Start Tower
Moving Disk from Intermediate Tower to End Tower
Moving Disk from Start Tower to End Tower

Moving Disk from Start Tower to Intermediate Tower
Moving Disk from Start Tower to End Tower
Moving Disk from Intermediate Tower to End Tower
Moving Disk from Start Tower to Intermediate Tower
Moving Disk from End Tower to Start Tower
Moving Disk from End Tower to Intermediate Tower
Moving Disk from Start Tower to Intermediate Tower
Moving Disk from Start Tower to End Tower
Moving Disk from Intermediate Tower to End Tower
Moving Disk from Intermediate Tower to Start Tower
Moving Disk from End Tower to Start Tower
Moving Disk from Intermediate Tower to End Tower
Moving Disk from Start Tower to Intermediate Tower
Moving Disk from Start Tower to End Tower
Moving Disk from Intermediate Tower to End Tower
"""
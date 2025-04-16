'''
the Tower of Hanoi is a classic mathematical puzzle that involves three rods and a number of disks of 
    different sizes which can slide onto any rod. 

The Problem:
-------------------------
You have three rods: usually named A (source), B (auxiliary), and C (destination).
You have n disks, each with a different size, and they are all initially stacked in decreasing size on rod A — the largest at the bottom, smallest at the top.
Your goal is to move the entire stack to rod C (destination), following three rules:

The Rules:
--------------------
Only one disk can be moved at a time.
Each move involves taking the top disk from one of the stacks and placing it on top of another stack.
No larger disk may be placed on top of a smaller disk.


'''

def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, destination, source)
    
n = 3  # Number of disks
tower_of_hanoi(n, 'A', 'C', 'B')

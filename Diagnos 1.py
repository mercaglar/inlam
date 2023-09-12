def print2(n):
    if not (1 <= n <= 99):
        print("N måste vara ett heltal mellan 1 och 99.")
    for i in range(2, n + 1):
        print(i)  
print2 (99)
import time

name = input("Enter name: ")

if name.lower() == "samta":
    for i in range(1, 1001):
        print(f"{i}: Ye to Madam Ji hain", end=" | ", flush=True)
        time.sleep(0.15)
else:
    print("Random User")

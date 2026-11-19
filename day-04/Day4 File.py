# A program that writes names
try:
with open("names.txt", "w") as f:
    f.write("Boledi\n")
    f.write("Mosa\n")
    f.write("Rea\n")
    f.write("Kgethego\n")
    f.write("Ditheto\n")
    
f = open("names.txt", "r")
text = f.read()
f.close()

# Read and display information    
        
with open("names.txt") as f:
    for line in f:
        print(line.strip())

names ="Boledi, Mosa, Rea, Kgethego, Ditheto"        
print(names.strip().upper())

with open("names.txt", "a") as f:
    f.write("Onnica\n")
with open("names.txt") as f:
    lines = f.readlines()
    print(len(lines))
    
    with open("nothing.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found. Check the name and folder.")
    

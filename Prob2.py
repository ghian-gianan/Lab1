filename = input("Enter FIle Name: ")
lines = []

with open(filename, 'r') as f:
    for line in f:
        lines.append(line.strip())
        
while True:
    print("The file has", len(lines), "lines.")
    if len(lines) == 0:
        break
    lineNumber = int(input("Enter a line number [0 to quit]: "))
    if lineNumber == 0:
        break
    elif lineNumber == lin(lines):
        print ("Error: line number must be less than or equal to ", len(lines))
    else:
        print(lineNumber, ":", lines[lineNumber -1])
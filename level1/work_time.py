import sys

result = 0

for i in range(5):
    start, end = sys.stdin.readline().split()

    start_HH = int(start.split(':')[0])
    start_MM = int(start.split(':')[1])
    end_HH = int(end.split(':')[0])
    end_MM = int(end.split(':')[1])

    if (end_MM < start_MM):
        HH = end_HH - start_HH - 1
        MM = 60 + (end_MM - start_MM)
    else:
        HH = end_HH - start_HH
        MM = end_MM - start_MM
        
    result += HH*60 + MM

print(result)

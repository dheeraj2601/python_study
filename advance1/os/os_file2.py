from sys import argv

filename = input("Please enter the name of a file: ")
f = open(filename,'r')

d1ct = dict()
print("Number of times each animal visited each station:")
print("Animal Id           Station 1           Station 2")

for line in f:
     if '\n' == line[-1]:
          line = line[:-1]
     (AnimalId, Timestamp, StationId,) = line.split(':')
     key = (AnimalId,StationId,)
     if key not in d1ct:
          d1ct[key] = 0
     d1ct[key] += 1

# Enter your code here. Read input from STDIN. Print output to STDOUT
tup = input().split(' ')
N, M = int(tup[0]), int(tup[1])

#Let's start with the first line
first = int((M-3) / 2)
pat = '.|.'

for n in range(int(N/2)):
    print((first-3*n) *'-' + (2*n + 1)*pat + (first-3*n) *'-')

print(int((M-7)/2) * '-' + 'WELCOME' + int((M-7)/2) * '-')

for n in range(int(N/2)-1, -1, -1):
    print((first-3*n) *'-' + (2*n + 1)*pat + (first-3*n) *'-')

"""
[ 1 ]
data = [1,2,3,6,7,7]

data = sorted(data)
for i in range(len(data)-1):
    data.append(abs(data.pop()-data.pop()))
    sorted(data)
print(data)

"""

"""
[ 2 ]

i = 5
j = 9
k = 6

sum1 = int(((j - i + 1)/2)*(i + j)) + int(((j - k + 1)/2)*(j + k)-j)

n/2 (f + l)
n = f-l +1
print(sum1)

"""

"""
[ 3 ]

s1 = [1, 2, 3, 4, 5]
s2 = [5, 4, 3, 2, 1]

n, s, b = (len(s1), s1, s2) if len(s1) < len(s2) else (len(s2), s2, s1)

upC ,max_= 0,0

for i in range(len(s)):
    if s[i] == b[i] and max_ == 0:
        max_ = b[i]
        upC += 1
    if s[i] == b[i] and max_ < b[i]:
        upC += 1

print(upC)

"""
a = [1,2,3]
b=[i+1 for i in a]
print(b)
#lam lai voi kí tu
c='truong'
d=[i for i in c]
print(d)
#lam việc với random
e=[i for i in range(1,10)]
print(e)
#làm việc ới list
f = ['truong','tuyen','khang','hoa']
g=[i for i in f if i == 'truong'];print(g)
k=[i.title() for i in f if len(i) <5];print(k)
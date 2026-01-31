def c_n(cc,no):
    return (cc*0.4)+(no*0.6)
def overall(n1,n2,n3,n4,n5,n6,n7):
    return (n1+n2+n3+n4+n5+n6+n7)/16

x = input("arche cc")
y = input("arche note")
AR = c_n(float(x),float(y))
print("arche not " +str(AR))
x = input("logice cc")
y = input("logice note")
lo = c_n(float(x),float(y))
print("logece not " +str(lo))
x = input("graphe cc")
y = input("graphe note")
gr = c_n(float(x),float(y))
print("graphe not " +str(gr))
x = input("sisteme cc")
y = input("sisteme note")
si = c_n(float(x),float(y))
print("sisteme not " +str(si))
x = input("algo cc")
y = input("algo note")
al = c_n(float(x),float(y))
print("algo not " +str(al))
x = input("numeric cc")
y = input("numeric note")
nu = c_n(float(x),float(y))
print("numeric not " +str(nu))
en = input("engliche not")
x1 = float(al)*3
x2 = float(AR)*3
x3 = float(lo)*2
x4 = float(gr)*2
x5 = float(si)*3
x6 = float(en)*1
x7 = float(nu)*2
ov = overall(x1,x2,x3,x4,x5,x6,x7)
print("yuor overall is " + str(ov))


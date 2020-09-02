def fillPlaintext():
    abc="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    return abc.split(",")

def fillEncodeText():
    abc="D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,A,B,C"
    return abc.split(",")

def getValue(o,d,c):
    return d[o.index(c)]

#print(fillPlaintext())
#print(fillEncodeText())
print("Ingrese palabra")
w=input()
print("1. Cifrar")
print("2. Descifrar")
t=input()

o=[]
d=[]
if(t=="1"):
    w=w.lower()
    o=fillPlaintext()
    d=fillEncodeText()
elif(t=="2"):
    o=fillEncodeText()
    d=fillPlaintext()

r=""
for l in w:
    r=r+getValue(o,d,l)

print("resultado: " + r)
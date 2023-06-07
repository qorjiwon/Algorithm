a, b = map(int, input().split())

def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)
    
gcd_ = gcd(max(a,b), min(a,b))
print(gcd_, a*b//gcd_, end='\n')
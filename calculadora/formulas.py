def rad (n,r):
    return n *(1/r)

def expo (b,p):
    return b**p

def fat (n):
    for c in rang(n-1,0,-1):
        n = n*c
        return n

def radiano (n):
    return n*Pi/180

def grau (n):
    return n*180/Pi

def fha (n):
    return (n*9/5)+32

def cel (n):
    return (n-32)*5/9

Pi = 3.15156


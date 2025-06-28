a = lambda a : a+10
print(a(5))
X = lambda a: a-3
print(X(3))
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
def number(n):
  return lambda a: a + n

Term = number(3)
print(Term(2))
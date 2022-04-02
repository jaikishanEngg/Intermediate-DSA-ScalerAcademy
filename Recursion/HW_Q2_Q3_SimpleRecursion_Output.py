class Solve:
    def bar(self, x,y):
        if y == 0:
            return 0
        else:
            return x + self.bar(x, y-1)
    
    def foo(self, x, y):
        if y == 0:
            return 1
        else:
            return self.bar(x, self.foo(x, y-1))
    
    def fun(self, x, n):
        if n == 0:
            return 1
        elif n%2 == 0:
            return self.fun(x*x, n//2)
        else:
            return x * self.fun(x*x, (n-1)//2)

s = Solve()
print(s.foo(3,5))
print(s.fun(2,10))
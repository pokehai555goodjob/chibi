from exp import Val, Add
def parse(s: str):
    num = int(s)
    return Val(num)

e = parse("123")
print(e)

s = "1+2"
pos = s.find('+')
print('pos', pos)

s1 = s[0:pos]
s2 = s[pos+1:]
print(s1, s2)

class Add(object):
    __slots__=['left', 'right']
    def __init__(self,a ,b):
        self.left =a
        self.right=b
    def eval(self):
        return self.left.eval() + self.right.eval()

e =Add(Val(1), Val(2))
print(e.eval())
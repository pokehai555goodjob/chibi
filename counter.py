class Counter(object):
    def __init__(self): #コンストラクタ
        self.cnt=0
    def count(self):
        self.cnt += 1

    def doublecount(self):
    ＃2回カウントする
    pass

    def reset(self):
        self.cnt=0

    def show(self):
        print(self.cnt)

    def __repr__(self):
        return str(self.cnt)

c=Counter()
c.show()
c.doublecount()
c.show()
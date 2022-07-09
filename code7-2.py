class School:
    def __init__(self):
        self.count = int(input())
        self.ages = list(map(int, input().split()))
        self.heights = list(map(int, input().split()))
        self.weights = list(map(int, input().split()))

    def avg_ages(self):
        self.mage = sum(self.ages)/self.count
        return self.mage

    def avg_heights(self):
        self.mheight = sum(self.heights)/self.count
        return self.mheight

    def avg_weights(self):
        self.mweight = sum(self.weights)/self.count
        return self.mweight

    def get_info(self):
        print("%.1f" % self.avg_ages())
        print("%.1f" % self.avg_heights())
        print("%.1f" % self.avg_weights())


sch1 = School()
sch2 = School()

sch1.get_info()
sch2.get_info()

inf = [[sch1.mheight, sch1.mweight, 'A'], [sch2.mheight, sch2.mweight, 'B']]
inf.sort(key=lambda x: x[1])
inf.sort(key=lambda x: x[0], reverse=True)

if inf[0][:2] == inf[1][:2]:
    print('Same')
else:
    print(inf[0][2])

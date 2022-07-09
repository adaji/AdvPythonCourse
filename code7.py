class School:
    def __init__(self):
        self.count = int(input())
        self.ages = list(map(int, input().split()))
        self.heights = list(map(int, input().split()))
        self.weights = list(map(int, input().split()))

    def avg_ages(self):
        return sum(self.ages)/self.count

    def avg_heights(self):
        return sum(self.heights)/self.count

    def avg_weights(self):
        return sum(self.weights)/self.count

    def get_info(self):
        print("%.1f" % self.avg_ages())
        print("%.1f" % self.avg_heights())
        print("%.1f" % self.avg_weights())


sch1 = School()
sch2 = School()

sch1.get_info()
sch2.get_info()

if sch1.avg_heights() > sch2.avg_heights():
    print('A')
elif sch1.avg_heights() < sch2.avg_heights():
    print('B')
else:
    if sch1.avg_weights() < sch2.avg_weights():
        print('A')
    elif sch1.avg_weights() > sch2.avg_weights():
        print('B')
    else:
        print('Same')

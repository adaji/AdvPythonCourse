# games = ['3-2', '5-2', '2-2', '0-0', '0-1', '4-10']
class team():
    wins = 0
    loses = 0
    draws = 0
    goal_diffs = 0
    points = 0

    def __init__(self, name):
        self.name = name


def play(p1_obj, p2_obj, result):
    p1s, a, p2s = result.partition('-')

    p1 = int(p1s)
    p2 = int(p2s)

    p1_obj.goal_diffs += p1-p2
    p2_obj.goal_diffs += p2-p1
    if p1 > p2:
        p1_obj.wins += 1
        p2_obj.loses += 1

        p1_obj.points += 3
    elif p1 < p2:
        p2_obj.wins += 1
        p1_obj.loses += 1

        p2_obj.points += 3
    else:
        p1_obj.draws += 1
        p2_obj.draws += 1

        p1_obj.points += 1
        p2_obj.points += 1


# ------------------------------------


teams = [team('Spain'), team('Iran'), team('Portugal'), team('Morroco')]


for i in range(6):
    scores = input()

    if i == 0:
        play(teams[1], teams[0], scores)
    elif i == 1:
        play(teams[1], teams[2], scores)
    elif i == 2:
        play(teams[1], teams[3], scores)
    elif i == 3:
        play(teams[0], teams[2], scores)
    elif i == 4:
        play(teams[0], teams[3], scores)
    elif i == 5:
        play(teams[2], teams[3], scores)

final = teams.sort(key=)

for x in teams:
    print('%s  wins:%d , loses:%d , draws:%d , goal difference:%d , points:%d'
          % (x.name, x.wins, x.loses, x.draws, x.goal_diffs, x.points))

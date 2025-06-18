name1, name2, name3 = str(input()), str(input()), str(input())

maxi = max(len(name1), len(name2), len(name3))
mini = min(len(name1), len(name2), len(name3))

if mini == len(name1): print(name1)
elif mini == len(name2): print(name2)
elif mini == len(name3): print(name3)
if maxi == len(name1): print(name1)
elif maxi == len(name2): print(name2)
elif maxi == len(name3): print(name3)

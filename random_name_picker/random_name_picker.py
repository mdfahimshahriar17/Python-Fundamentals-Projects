import random

friends = ["Fahim", "Shahriar", "Salman", "Rafid", "Neha", "Suprio", "Talha"]

#Self try before knowing the method
check_nmber_of_friends = len(friends)

#if we don't use -1 it will give an index error
random_friends = random.randint(0, check_nmber_of_friends-1)
print(friends[random_friends])



# 1 Option
print(random.choice(friends))





# 2nd Option
random_index = random.randint(0, 6)
print(friends[random_index])
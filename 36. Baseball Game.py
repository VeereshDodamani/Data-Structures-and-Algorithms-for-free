# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.


ops = ["5","2","C","D","+"]
ops1 = []
for i in ops:
    if i == "+":
        ops1.append(ops1[-1]+ops1[-2])
    elif i=="D":
        ops1.append(ops1[-1]*2)
    elif i=="C":
        ops1.pop()
    else:
        ops1.append(int(i))
print(sum(ops1)) 

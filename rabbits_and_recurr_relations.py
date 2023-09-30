def rabbits(months,offspring):
    parent,child= 1,1
    for itr in range(months-1):
        child,parent=parent,parent+(child*offspring)
    return child

print(rabbits(36,3))
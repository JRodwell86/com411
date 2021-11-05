import random
#empty list
my_list = []
#will only choose numbers between 1 and 50
max_val = random.randint(1, 50)
#will print a list of random numbers, including duplicates that is between 100 and 10000 number long
for i in range(random.randint(100, 10000)):
    my_list.append(random.randint(1, max_val))

print(my_list)
print(len(my_list))
print(max(my_list))
#will turn it in to a set (set(my_list) to get rid of duplicates because it only has originals
#(list(set(my_list))) will turn it back in to a list
print(list(set(my_list)))

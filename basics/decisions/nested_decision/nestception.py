#ask user where to look
look = input("Where should I look? (in the bedroom/in the bathroom/in the lab/somewhere else")
if look == "in the bedroom":
#ask user where in bedroom to look
    bedroom_look = input("Where in the bedroom should I look?(under the bed/anywhere else)")
    if bedroom_look == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found mess but no battery")
elif look == "in the bathroom":
#ask user where in bathroom to look
    bathroom_look = input("Where in the bathroom should I look? (in the bathtub/anywhere else)")
    if bathroom_look == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("found a wet surface but no battery")
elif look == "in the lab":
    #ask where in lab to look
    lab_look = input("Where in the lab should I look? (on the table/anywhere else)")
    if lab_look == "on the table":
        print("Yes! I found my battery")
    else:
        print("found some tools but no battery")
else:
    print("I do not know where that is but I will keep looking.")
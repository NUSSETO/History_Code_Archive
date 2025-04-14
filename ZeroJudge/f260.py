# ZeroJudge f260: Gossip
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=f260

while True:
  try:
    num_classmate, num_relation = map(int, input().split())
    mylist = []
    mylist.append(set(map(int, input().split()))) # The element in the list is a set

    for i in range(num_relation - 1): # Since we already put 1 relation in the list
      relation_set = set(map(int, input().split()))
      indicator = 0 # Check if the relation is intersected or not
      for j in range(len(mylist)):
        if relation_set.intersection(mylist[j]) != set():
          mylist[j] = mylist[j].union(relation_set)
          indicator = 1
      if indicator == 0:
        mylist.append(relation_set)

    for i in range(num_classmate): 
      indicator = 0 # Check if someone is not in any relation
      for j in range(len(mylist)):
        if i in mylist[j]:
          indicator = 1 
      if indicator == 0:
        mylist.append({i})
        
    print(len(mylist))
  except:
    break # End of input

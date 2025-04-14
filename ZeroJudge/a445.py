# ZeroJudge a445: I have few friends
# Problem Link: https://zerojudge.tw/ShowProblem?problemid=a445

while True:
  try:
    num_people, num_relation, num_inquiry = map(int, input().split())
    mylist = []
    mylist.append(set(map(int, input().split()))) # The elements in the list are sets.
    
    for i range(num_relation - 1): # Since we already appen one set into the list.
      relation_set = set(map(int, input().split()))
      counter = 0 # Check how many times the set have intersected with the sets in list.
      union_set = [] # Store sets in list that intersected with the current set.
    
      for j in range(len(mylist)):
        if relation_set.intersection(mylist[j]) != set():
          mylist[j] = mylist[j].union(relation_set)
          union_set.append(mylist[j])
          counter += 1
          
      if counter == 0: # Donesn't intersect at all.
        mylist.append(relation_set)
      elif counter > 1: # Intersect more than once.
        fset1 = set(map(frozenset, mylist))
        fset2 = set(map(frozenset, union_set))
        diff_set = fset1 - fset2
        diff_list = list(map(set, diff_set)) # Extract those doesn't intersect
        
        for j in range(1, len(union_set)):
          union_set[0] = union_set[0].union(union_set[j]) # Just make everybody in one set
          
        mylist = [union_set[0], *diff_list]  # Make mylist more simplified

    for i in range(num_inquiry):
      inquiry_set = set(map(int, input().split()))
      indicator = 0 # Check if in a relation or not
      
      for j in range(len(mylist)):
        if inquiry_set.issubset(mylist[j]):
          indicator = 1

      if indicator == 1:
        print(':)')
      else:
        print(':(')
        
  except:
    break # End of input

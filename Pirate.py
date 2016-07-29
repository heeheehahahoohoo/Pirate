print "Arr, matey"
for i in range(100):
  print str(i) + " bottles of rum"
  
  with open('Treasure.txt') as fh:
  for line in fh:
    print line
width = 10
height = 10

rows = [
  'ihlqeaooxfmicfc',
  'cbatyvnxjimcllh',
  'mcpgeracgoilarp',
  'mpakjvauesuidwf',
  'ufcsigetuslrfdv',
  'eshrrlamiithnvq',
  'rekcbytbmugolea',
  'thteellaungjrty',
  'ogenlffideadssk',
  'snriaecemtleime',
  'pinwydtbnaiiiap',
  'wgeococoxffctmr',
  'gnsggwdgnmgozas',
  'aitfrebmemerowh',
  'osoopnbpapathvu']

map = []
for num in range(len(rows)):
  map.append(list(rows[num]))
print(map)
words = ['abuelita, alebrije', 'ancestors', 'coco', 'dante', 'dead', 'ernesto', 'familia', 'family', 'fiesta', 'guitar', 'journey', 'mama', 'miguel', 'muertos', 'music', 'papa', 'remember', 'singing', 'skeleton']

def findWord(word):
  x, y = [], []
  target = word[0]
  possibleMatches = []
  slopes = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]


  global map
  for row in map:
    if target in row:
      x.append(row.index(target))
      y.append(map.index(row))

  for num in range(len(x)):
    for slope in slopes:
      possibleMatch = ''
      tx, ty = x[num], y[num]
      try:
        for char in range(len(word)):
          possibleMatch += map[ty][tx]
          tx += slope[0]
          ty += slope[1]
        if possibleMatch == word:
          return slope, x[num], y[num]
      except: pass
    
findWord('coco')

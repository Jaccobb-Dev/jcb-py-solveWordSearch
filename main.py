width = 10
height = 10

wsr1 = [
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
wsr2 = [
  'ALREVIDDCSNBUOXS',
  'LAIVTJFIECAENUWC',
  'LITIGATINGLGSTJR',
  'ERCLEAREDBAUESEE',
  'YEOOGOSAABUNEMTW',
  'YTNACSBTKJWIMAOD',
  'ESDIETITIANILRIR',
  'LIGISMOXUBLUITHI',
  'BGSDIMWITSGMEIFV',
  'AASNUBBEDNEOSNRE',
  'RMIYMSPRATFLTGIR',
  'OMETUBIRTSIDERLF',
  'DEILPITLUMXLISLE',
  'ALSESSELPARTSUSW'
]

wsw1 = ['abuelita', 'alebrije', 'ancestors', 'coco', 'dante', 'dead', 'ernesto', 'familia', 'family', 'fiesta', 'guitar', 'journey', 'mama', 'miguel', 'muertos', 'music', 'papa', 'remember', 'singing', 'skeleton']

wsw2 = 'ADORABLE AGED ALLEY BAAS BAIT BEGUN BUXOM CESIUM CLEARED CLUE DIETITIAN DIMWIT DIVER FINE FOETID FRILLS GISMO GOOEY INBUILT INIMITABLE JABS KARATE LEMMA LISLE LITIGATING LIVE MAGISTERIAL METTLE MULTIPLIED OBTUSE OMEGAS OUTSMARTING REDISTRIBUTE SCANTY SCREWDRIVER SLIMMER SNUBBED SPRAT STRANGULATE STRAPLESSES UNSEEMLIEST USELESS VIAL'.split()

map = []
rows, words = wsr2, wsw2
for num in range(len(rows)):
  map.append(list(rows[num]))
print(map)


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
    
matches = []
for word in words:
  try:
    s, x, y = findWord(word)
    matches.append([word, s, x, y])
  except:
    matches.append([word, 'Not Found'])

for match in matches:
  print(match)
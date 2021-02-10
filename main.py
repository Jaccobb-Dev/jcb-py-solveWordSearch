import random, os, time

os.system('cls')

class wordSeachSolver:

    def __init__(self):

        self.colors = [
            '\033[95m', # Purple
            '\033[94m', # Blue
            '\033[93m', # Yellow
            '\033[92m', # Green
            '\033[91m'  # Red
        ]

        self.clearColor = '\033[0m'

        self.slopes = [
            [0,  -1],
            [0,   1],
            [-1,  0],
            [1,   0],
            [-1,  1],
            [1,  -1],
            [-1, -1],
            [1,   1]
        ]

        self.slopeDirections = [
            'up',
            'down',
            'left',
            'right',
            'left and down',
            'right and up',
            'left and up',
            'right and down'
        ]

        self.algorithms = [
            'slope',
            'random'
        ]

        self.algorithmFunctions = [
            self.slopeSolve,
            self.randomSolve
        ]

    def solve(self, rows, words, algorithm = 0):

        # Determine Algorithm
        if algorithm != 0: 
            algorithm = self.algorithms.index(algorithm)
        algorithmFunction = self.algorithmFunctions[
            algorithm]

        # Convert Rows to Map
        map = []
        for row in rows:
            splitRow = list(row.lower())
            finalList = []
            for char in splitRow:
                finalList.append([char, False, self.clearColor])
            map.append(finalList)

        # Ensure Words are Lowercase
        for word in words:
            words[words.index(word)] = word.lower()

        # Run Selected Algorithm
        clearMap, wordCoordinates = algorithmFunction(map, words)
        
        while True:
          self.printPuzzle(clearMap, wordCoordinates)
        
          try:
            x = int(input("Pick a Word: "))
          except: continue
        
          map = self.highlightWords(map, [words[x]], wordCoordinates)

          # Display Solved Puzzle
          self.printPuzzle(map, wordCoordinates)
          
          time.sleep(5)
      
    def highlightWords(self, map, words, wordCoordinates):
      
      for word in words:
        selectedColor = random.choice(self.colors)
        for wordData in wordCoordinates:
          if word == wordData[0]:
            word, slope, x, y = wordData
            break
        for num in range(len(word)):
          map[y+(slope[1]*num)][x+(slope[0]*num)][1] = True
          map[y+(slope[1]*num)][x+(slope[0]*num)][2] = selectedColor
      
      return map

    def printPuzzle(self, solvedPuzzle, wordCoordinates):

        for y in range(len(solvedPuzzle)):
            row = ''
            for x in range(len(solvedPuzzle[1])):
                color = self.clearColor
                if solvedPuzzle[y][x][1] == True: color = solvedPuzzle[y][x][2]
                row += color + solvedPuzzle[y][x][0] + color + '  '
            print(row)

        for wordData in wordCoordinates:
            try:
                word, slope, x, y = wordData
                print(f'{word} is at {x}, {y} pointing {self.slopeDirections[self.slopes.index(slope)]}')
            except: print(f'{wordData} was not found')

    def slopeSolve(self, map, words):
      
        #words = ['aged']

        mapX, mapY = len(map[0]), len(map)
        wordCoordinates = []

        for word in words:
            targetLetter = word[0:1]
            for y in range(mapY):
                for x in range(mapX):
                    if map[y][x][0] == targetLetter:
                        for slope in self.slopes:
                            possibleMatch = ''
                            targetX, targetY = x, y
                            try:
                                for charNum in range(len(word)):
                                    possibleMatch += map[targetY][targetX][0]
                                    targetX += slope[0]
                                    targetY += slope[1]
                                if possibleMatch == word:
                                    wordCoordinates.append([word, slope, x, y])
                            except: pass
        return map, wordCoordinates

    def randomSolve(self, map, words):
        print('random')
        print(map, words)

wsm = [
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
  'osoopnbpapathvu'
]
'''
wsm = [
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
'''
wsw = [
    'abuelita', 
    'alebrije', 
    'ancestors', 
    'coco', 
    'dante', 
    'dead', 
    'ernesto', 
    'familia', 
    'family', 
    'fiesta', 
    'guitar', 
    'journey', 
    'mama', 
    'miguel', 
    'muertos', 
    'music', 
    'papa', 
    'remember', 
    'singing', 
    'skeleton'
]

#wsw = 'ADORABLE AGED ALLEY BAAS BAIT BEGUN BUXOM CESIUM CLEARED CLUE DIETITIAN DIMWIT DIVER FINE FOETID FRILLS GISMO GOOEY INBUILT INIMITABLE JABS KARATE LEMMA LISLE LITIGATING LIVE MAGISTERIAL METTLE MULTIPLIED OBTUSE OMEGAS OUTSMARTING REDISTRIBUTE SCANTY SCREWDRIVER SLIMMER SNUBBED SPRAT STRANGULATE STRAPLESSES UNSEEMLIEST USELESS VIAL'.split()

solver = wordSeachSolver()
solver.solve(wsm, wsw)
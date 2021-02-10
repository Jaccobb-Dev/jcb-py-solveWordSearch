import random, os

os.system('cls')

class wordSeachSolver:

    def __init__(self):

        colors = [
            '\033[95m',
            '\033[94m',
            '\033[93m',
            '\033[92m',
            '\033[91m'
        ]

        self.clearColor = '\033[0m'
        self.selectedColor = random.choice(colors)

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
                finalList.append([char, False])
            map.append(finalList)

        # Ensure Words are Lowercase
        for word in words:
            words[words.index(word)] = word.lower()

        # Run Selected Algorithm
        solvedPuzzle, wordCoordinates = algorithmFunction(map, words)

        # Display Solved Puzzle
        self.printSolvedPuzzle(solvedPuzzle, wordCoordinates)

    def printSolvedPuzzle(self, solvedPuzzle, wordCoordinates):

        for y in range(len(solvedPuzzle)):
            row = ''
            for x in range(len(solvedPuzzle[1])):
                color = self.clearColor
                if solvedPuzzle[y][x][1] == True: color = self.selectedColor
                row += color + solvedPuzzle[y][x][0] + color + '  '
            print(row)

        for wordData in wordCoordinates:
            try:
                word, slope, x, y = wordData
                print(f'{word} is at {x}, {y} pointing {self.slopeDirections[self.slopes.index(slope)]}')
            except: print(f'{wordData} was not found')

    def slopeSolve(self, map, words):

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
                            coords = [[x, y]]
                            try:
                                for charNum in range(len(word)):
                                    possibleMatch += map[targetY][targetX][0]
                                    targetX += slope[0]
                                    targetY += slope[1]
                                    coords.append([targetX , targetY])
                                if possibleMatch == word:
                                    wordCoordinates.append([word, slope, x, y])
                                    for solvedX, solvedY in coords:
                                        map[solvedY][solvedX][1] = True
                            except: pass
        while True:
            for num in range(len(words)):
                if not wordCoordinates[num][0] == words[num]:
                    wordCoordinates.insert(num, words[num])
                    break
            break
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

wsw = 'ADORABLE AGED ALLEY BAAS BAIT BEGUN BUXOM CESIUM CLEARED CLUE DIETITIAN DIMWIT DIVER FINE FOETID FRILLS GISMO GOOEY INBUILT INIMITABLE JABS KARATE LEMMA LISLE LITIGATING LIVE MAGISTERIAL METTLE MULTIPLIED OBTUSE OMEGAS OUTSMARTING REDISTRIBUTE SCANTY SCREWDRIVER SLIMMER SNUBBED SPRAT STRANGULATE STRAPLESSES UNSEEMLIEST USELESS VIAL'.split()

solver = wordSeachSolver()
solver.solve(wsm, wsw)
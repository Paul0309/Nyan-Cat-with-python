from winsound import Beep
import time

def freq(o, s):
    if s == "C" or s == "c":            #도
        return 524*2**o
    elif s == "C#" or s == "c#":         #도샾 
        return 554*2**o
    elif s == "D" or s == "d":          #레
        return 587*2**o
    elif s == "D#" or s == "d#":         #레샾
        return 622*2**o
    elif s == "E" or s == "e":          #미
        return 659*2**o
    elif s == "F" or s == "e#":          #파
        return 698*2**o
    elif s == "F#" or s == "f#":         #파샾   
        return 740*2**o
    elif s == "G" or s == "g":          #솔
        return 784*2**o
    elif s == "G#" or s == "g#":         #솔샾   
        return 831*2**o
    elif s == "A" or s == "a":          #라 
        return 880*2**o
    elif s == "A#" or s == "a#":         #라샾   
        return 932*2**o
    elif s == "B" or s == "b":          #시
        return 988*2**o

def tempo(sec):
    t = 700
    d = 80
    return int((sec*t)-d)

def rest(sec):
    t = 700
    d = 80
    return time.sleep((t*sec-d)/1000)

def beep(octave, pitch, beat):
    if pitch == "REST":
        rest(0.25)
    else:
        return Beep(freq(octave, pitch), tempo(beat))

pitchLst = ["F", "G", "D", "D", "REST", "A#", "D", "C", "A#", "REST", "A#", "C", "D", "D", "C",
            "A#", "C", "D", "F", "G", "D", "F", "C", "D", "A#", "C", "A#", "D", "F", "G", "D", "F", "C", "D", "A#", "C", "D",
            "C", "A#", "A#", "C", "D", "D", "C", "A#", "C", "D", "F", "G", "D", "F", "C", "D"]
                                         #여기                                   #여기
beatLst = ["0.5", "0.5", "0.25", "0.25", "0.25", "0.25", "0.25", "0.25", "0.25", "0.25", "0.5", "0.5", "0.5", "0.25", "0.25", "0.25",
            "0.25", "0.25", "0.25", "0.25", "0.25", "0.25", "0.25", "0.25", "0.25", "0.25", "0.25", "0.5", "0.5", "0.25", "0.25", "0.25", "0.25", "0.25",
            "0.25", "0.25", "0.25", "0.25", "0.25", "0.25", "0.25", "0.5", "0.25", "0.25", "0.25", "0.25", "0.25", "0.25", "0.25", "0.25", "0.25", "0.25", "0.25"]
octaveLst = [1, 1, 1, 1, 10, 0, 1, 1, 0, 10, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0,
            1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0,
            1, 1, 1, 1, 1, 1, 1, 1]
#샘플: Beep(freq(0, "도"), tempo(1))
'''
도 도샾 레 레샾 미 파 파샾 솔 솔샾 라 라샾 시
C  C#   D  D#   E  F  F#   G  G#   A  A#   B

1       = 1/4
0.5     = 1/8
0.25    = 1/16
0.125   = 1/32
'''
restVar = "01110010011001010111001101110100"
j = 0
for i in pitchLst:
    beep(octaveLst[j], i, float(beatLst[j]))
    #print(octaveLst[j], i, float(beatLst[j]))
    j += 1
print(len(pitchLst), len(beatLst), len(octaveLst))

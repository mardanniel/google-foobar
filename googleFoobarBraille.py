#LEVEL 1 CHALLENGE - BRAILLE

def solution(s):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','blank',"caps"]
    lettersCaps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','BLANK','CAPS']
    lettersBraille = ["100000","110000","100100","100110","100010","110100","110110","110010","010100","010110","101000","111000","101100","101110","101010","111100","111110","111010","011100","011110","101001","111001","010111","101101","101111","101011", "000000", "000001"]
    contructedString = ""
    for i in range(len(s)):
        for j in range(len(lettersBraille)):
            if s[i] == letters[j]:
                contructedString += lettersBraille[j]
            elif s[i] == lettersCaps[j]:
                contructedString += lettersBraille[27]
                contructedString += lettersBraille[j]
            elif s[i] == " ":
                contructedString += lettersBraille[26]
                break
    return contructedString

print(solution("test Asdq"))


#import re

class Solution:
    def mostCommonWord(self, paragraph, banned):
        wordMap = {}
        
        #paragraph = re.sub('[^A-Za-z]', ' ', paragraph)
        
        formalString = ''
        for c in paragraph:
            if(c.isalpha()):
                formalString += c.lower()
            else:
                formalString += ' '
        paragraph = formalString
        
        #paragraph = paragraph.replace(',', ' ')
        banned = [w.lower() for w in banned]
        for word in paragraph.lower().split():
            word = word.strip("!?',;.")
            if(word not in banned):
                if(word in wordMap):
                    wordMap[word] += 1
                else:
                    wordMap[word] = 1
                    
        ans, best = [], 0
        for word in wordMap:
            if(wordMap[word] > best):
                ans, best = [word], wordMap[word]
            elif(wordMap[word] == best):
                ans.append(word)
        return ans
        

if __name__ == '__main__':

    paragraph = "Bob hit a ball, the hit BALL bOb  Flew flew far after it was hit."
    banned = ["hit"]

    S = Solution()
    print(Solution.mostCommonWord(S, paragraph, banned))

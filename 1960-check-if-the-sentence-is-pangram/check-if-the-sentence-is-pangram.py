class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence=sentence.lower()
        # freq={}
        # if len(sentence)<26:
        #     return False

        # else:
        #     for  i in sentence:
        #         if i in freq:
        #             freq[i]+=1
        #         else:
        #             freq[i]=1
        # return len(freq)==26
        ch=set()
        for i in sentence:
            ch.add(i)
        return len(ch)==26
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def is_valid(word1,word2):
            return sum(c1!=c2 for c1,c2 in zip(word1,word2)) == 1

        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        fqueue=deque([beginWord])
        bqueue=deque([endWord])
        fvisited={beginWord:1}
        bvisited={endWord:1}

        while fqueue and bqueue:
            if len(fqueue) > len(bqueue):
                fqueue,bqueue=bqueue,fqueue
                fvisited,bvisited=bvisited,fvisited

            for _ in range(len(fqueue)):
                word=fqueue.popleft()
                curr_count=fvisited[word]

                for i,w in enumerate(word):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c==w:
                            continue
                        next_word=word[:i]+c+word[i+1:]

                        if next_word in bvisited:
                            return curr_count+bvisited[next_word]
                        
                        if next_word in wordSet and next_word not in fvisited:
                            fvisited[next_word]=curr_count+1
                            fqueue.append(next_word)
                            wordSet.remove(next_word)


        return 0
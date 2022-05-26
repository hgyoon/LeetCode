class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #base condition where the row is 1
        if numRows == 1:
            return s
        output = ""
        rank = 0
        #we're going to use this to go back and forth
        rank_mover = 1
        combined_by_rank = [""] * numRows
        for i in range(len(s)):
            combined_by_rank[rank] += s[i]
            #after adding a letter, move the row higher/lower
            rank += rank_mover
            #when the rank reaches the highest or lowest
            if rank == 0 or rank == numRows -1:
                #flip the rank mover to go down/up
                rank_mover *= -1
        for i in range(numRows):
            output += combined_by_rank[i]
        return output

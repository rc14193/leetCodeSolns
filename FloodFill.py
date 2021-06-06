#https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1393/
# According to Trial 68 ms and 14.5 mb
# 95.45% time and 21.71% space

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        stack = [(sr,sc)]
        visited = {}
        valid_path_val = image[sr][sc]

        while stack:
            row, col = stack.pop()
            if image[row][col] == valid_path_val and not visited.get((row, col)):
                image[row][col] = newColor
                if row+1 < len(image):
                    stack.append((row+1,col))
                if row-1 >= 0:
                    stack.append((row-1,col))
                if col-1 >= 0:
                    stack.append((row,col-1))
                if col+1 < len(image[0]):
                    stack.append((row,col+1))
            visited[(row, col)] = True
        return image

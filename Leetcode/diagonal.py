# class Solution:  
#     def diagonalSum(self, mat: list[list[int]]) -> int:
#         store = len(mat) -1
#         math = len(mat)/2
#         answer = []
        
#         for i in range(store+1):
            
#             # Finding ascending
#             ind_pos = mat[store][store]
#             print("ascending ind_pos is", ind_pos)
            
#             answer.append(ind_pos)
            
#             # Finding descending
#             inverse_mat = mat[::-1]
#             desc_ind_pos = inverse_mat[store][store]
#             print("descending ind_pos is", desc_ind_pos)
#             answer.append(desc_ind_pos)
#             store = store - 1
            
            
#         if math % 2 == 0:
#             print (sum(answer))
#             return sum(answer)
#         else: 
#             rm = len(answer)
#             rm_f = answer[rm // 2]
#             print (sum(answer))
#             return sum(answer) - rm_f
            
#     mat = [[6,3,1,10,7,4],[4,10,1,9,5,10],[5,5,7,3,8,5],[2,7,6,4,7,6],[7,9,6,1,8,5],[1,7,9,5,8,4]]
#     diagonalSum(diagonalSum, mat)
    
    
    # Better version....
    # 
    # 
class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        result = 0
        for i in range(n):
            result += mat[i][i] + mat[i][n - i - 1]
        if n % 2 == 1:
            result -= mat[n // 2][n // 2]
        return result
    
    mat = [[6,3,1,10,7,4],[4,10,1,9,5,10],[5,5,7,3,8,5],[2,7,6,4,7,6],[7,9,6,1,8,5],[1,7,9,5,8,4]]
    diagonalSum(diagonalSum, mat)
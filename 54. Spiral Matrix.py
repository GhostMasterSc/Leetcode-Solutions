class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)-1
        m = len(matrix[0])-1
        m_r=0
        n_r=1
        return_array=[]
        length = len(matrix)*len(matrix[0])
        r=0
        c=-1
        direction="c"
        
        for i in range(length):
            if direction=="c":
                c+=1
                return_array.append(matrix[r][c])
                if c==m:
                    direction="r"
                    m-=1
            elif direction=="r":
                r+=1
                return_array.append(matrix[r][c])
                if r==n:
                    direction="-c"
                    n-=1
            elif direction=="-c":
                c-=1
                return_array.append(matrix[r][c])
                if c==m_r:
                    direction="-r"
                    m_r+=1
            elif direction=="-r":
                r-=1
                return_array.append(matrix[r][c])
                if r==n_r:
                    direction ="c"
                    n_r+=1


        return return_array


            
            

            


import numpy as np
import pandas as pd
class MathEngine:
    def determinant(self,matrix_target):
        matrix=matrix_target.get_matrix()
        # Convert to NumPy for calculation
        arr=np.array(matrix)
        return round(np.linalg.det(arr),2)
    
    def multiply(self,matrix_target_a,matrix_target_b):
        A = np.array(matrix_target_a.get_matrix())
        B = np.array(matrix_target_b.get_matrix())
        result = np.dot(A,B)
        return result.tolist()


import numpy as np
import pandas as pd

# Target Interface
class MatrixTarget:
    def get_matrix(self):
        """Return matrix as a nested list"""
        pass

# Adapter for NumPy
class NumPyAdapter(MatrixTarget):
    def __init__(self,np_matrix):
        self.np_matrix=np_matrix
    
    def get_matrix(self):
        # Convert NumPy arra to nested list
        return self.np_matrix.tolist()
    
# Adapter for Pandas
class PandasAdapter(MatrixTarget):
    def __init__(self,df_matrix):
        self.df_matrix=df_matrix

    def get_matrix(self):
        # Convert DataFrame to nested list
        return self.df_matrix.tolist()
    
import numpy as np
import pandas as pd
from source import NumPyAdapter,PandasAdapter
from client import MathEngine

# Usage Example
if __name__=="__main__":
    # NumPy matrix
    np_matrix=np.array([[1,2],[3,4]])
    np_adapter=NumPyAdapter(np_matrix)

    # Pandas DataFrame matrix
    df_matrix=pd.DataFrame([[5,6],[7,8]])
    pd_adapter=PandasAdapter(df_matrix)

    # Math Engine
    engine=MathEngine()

    # Determinant of NumPy matrix
    print("Determinant (NumPy): ",engine.determinant(np_adapter) )

    # Determinant of Pandas matrix
    print("Determinant (Pandas): ",engine.determinant(pd_adapter))

    # Mulitplication demo 
    print("Multiplication Result: ",engine.multiply(np_adapter,pd_adapter))
    
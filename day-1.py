import pandas as pd

# import numpy as np

if __name__ == "__main__":
    df = pd.read_csv("data/test.csv")
    print(df.columns.tolist()[0])

# import pandas as pd    
# import plotly.express as px

# def wrangle(filepath):
#     # Pre-exploration: only returning a dataframe object
#     return pd.read_csv(filepath)

# def wrangle(filepath):
#     df = pd.read_csv(filepath)    
#     df.fillna(0, inplace=True)
 
# if __name__ == '__main__':
#     df = wrangle(r'C:\Users\xende\Downloads\student+performance (1)\student\student-por.csv')
#     df.to_csv('student_cleaned.csv', index=False)




import pandas as pd    
import plotly.express as px
def wrangle(filepath):
    return pd.read_csv(filepath)
def wrangle(filepath):
    df = pd.read_csv(filepath)
    return df
if __name__ == '__main__':
    df = wrangle(r'C:\Users\xende\Downloads\student+performance (1)\student\student-por.csv')
    df.to_csv('student_cleaned', index=False)
import pandas as pd

def sort(path_1, path_2, type='Дата'):
    try:
        df1 = pd.DataFrame(pd.read_excel(path_1[0]))
        df2 = pd.DataFrame(pd.read_excel(path_2[0]))
        return (200, df1.append(df2, ignore_index=True, sort=False).sort_values(by=type))
    except Exception as error:
        return (503, error)




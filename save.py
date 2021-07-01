import pandas as pd

def save_table(file, path):
    df = pd.DataFrame(file)
    try:
        df.to_excel(f"{path[0]}.{path[1][1:]}", index=False)
        return 200
    except Exception as error:
        print(error)
        return 500
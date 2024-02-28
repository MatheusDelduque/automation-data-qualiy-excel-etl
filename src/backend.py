import pandas as pd
from contract import Sales

def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)

        extra_columns = set(df.columns) - set(Sales.__fields__.keys())
        if extra_columns:
            return False, f'Colunas extras: {", ".join(extra_columns)}'

        for index, row in df.iterrows():
            try: 
                _ = Sales(**row.to_dict())
            except Exception as e:
                raise ValueError(f'Erro na linha {index + 2}: {e}')
            
        return True, None
    
    except ValueError as ve:
        return False, str(ve)
    except Exception as e:
        return False, str(e)
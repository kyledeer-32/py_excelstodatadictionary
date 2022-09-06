import pandas as pd
#int, float, str, boolean

def df_excel_metadata(dict_dfs):

    for key in dict_dfs:
        df = pd.DataFrame(dict_dfs[key])
        print(df)
        for name, values in df.iteritems():
            #s = pd.Series([1, 2, '3', '67.0', '89.23', 't', 'forge', '', False, None])
            values = values.value_counts(normalize=True, dropna=False)

            val_percs = values.index.to_list()

            dtypes = {
                "<class 'str'>":0.0,
                "<class 'int'>":0.0,
                "<class 'float'>":0.0,
                "<class 'bool'>":0.0,
                "other":0.0  
            }

            for v in val_percs:

                t_str = str(type(v))

                if type(v) is str:
                    if '.' in v:
                        chk_float = v.replace('.', '')
                        if chk_float.isdigit() == True:
                            t_str = str(type(float(v)))
                    elif v.isdigit() == True:
                        t_str = str(type(int(v)))

                print('checking: ', t_str)

                try:
                    dtypes[t_str] = (dtypes[t_str] + s[v])
                except KeyError:
                    dtypes["other"] = (dtypes["other"] + s[v])

            print(dtypes)

            max_dtype = max(dtypes, key=dtypes.get)
            max_perc = dtypes[max_dtype]

            #if int dtype and float dtype compose majority dtype of column when combined - make dtype: float

            if max_dtype != "<class 'int'>" and max_dtype != "<class 'float'>":
                total_numperc = (dtypes["<class 'int'>"] + dtypes["<class 'float'>"])
                if total_numperc >= dtypes[max_dtype]:
                    max_dtype = "<class 'float'>"
                    max_perc = dtypes[max_dtype]







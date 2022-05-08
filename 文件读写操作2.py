import functools
import pandas as pd
import time

from openpyxl import Workbook, load_workbook


def time_cost(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        time_start = time.time()
        result = func(*args, **kw)
        time_end = time.time()
        timestrap = time_end - time_start
        print("function %s running time is %s" % (func.__name__, timestrap))
        return result

    return wrapper


@time_cost
def read_txt():
    dict1 = {}
    df1 = pd.read_csv(r"C:\Users\Administrator\Desktop\goods.txt")
    dict1 = df1.set_index("c_warecode").T.to_dict(orient="list")
    return dict1


@time_cost
def read_excel():
    wb = load_workbook(r"C:\Users\Administrator\Desktop\2.xlsx", data_only=True)
    sheet = wb.worksheets[0]
    for i in range(1000, 1, -1):
        sheet.delete_rows(i)

    wb.save(r"C:\Users\Administrator\Desktop\2.xlsx")


def row_item(item):
    pass


@time_cost
def read_excel2():
    df1 = pd.read_excel(r"C:\Users\Administrator\Desktop\2.xlsx")
    # print(df1.apply(row_item, axis=0))
    j = 0
    a = []
    for row in df1.itertuples():
        if j > 1000:
            a.append(j)
        j += 1
    print(a)
    df1.drop(a, axis=0, inplace=True)
    print(df1)
    df1.to_excel(r"C:\Users\Administrator\Desktop\2.xlsx", index=False)
    # dict1 = df1.to_dict("records")
    # print(dict1)
    # for row in dict1:
    #     print(row)
    # print(df1)


if __name__ == "__main__":
    # print("this is a test")
    # dict1 = read_txt()
    read_excel2()
    # print(dict1)

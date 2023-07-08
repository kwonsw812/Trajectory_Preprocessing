import pandas as pd
import numpy as np
import random

def get_IBRT_info(data: pd.DataFrame) -> dict[str, float]:
    drop_mask = (data.Global_X == -999)

    received_indices: np.ndarray = np.where(drop_mask == 0)[0]

    IBRT_list: np.ndarray = np.diff(received_indices) * 100

    return {
        # "all": IBRT_list,
        "average": IBRT_list.mean(),
        "max": np.max(IBRT_list),
        "std": np.std(IBRT_list),
        "min": 100 if np.all(IBRT_list == 100)
        else np.min([x for x in IBRT_list if x != 100]),
    }

#write your probability on this variable
probability = 0.05

dataframe = pd.read_csv("vehicle-trajectory-data/0750am-0805am/trajectories-0750am-0805am.csv")

i = 0
while i < len(dataframe):
    choice = random.choices(range(2), weights=[1-probability, probability])
    if choice == [1] :
        num_of_iter = random.randrange(100, 200)
        for j in range(num_of_iter):
            dataframe.loc[i, "Global_X"] = -999
            dataframe.loc[i, "Global_Y"] = -999
            i = i + 1

    # else :
    #     num_of_iter = random.randrange(0,99)
    #     for j in range(num_of_iter):
    #         dataframe.loc[i, "Global_X"] = -999
    #         dataframe.loc[i, "Global_Y"] = -999
    #         i = i + 1


print(get_IBRT_info(dataframe))

# print(dataframe[["Global_X", "Global_Y"]])
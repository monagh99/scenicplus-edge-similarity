import pickle
import pandas as pd

path = "../../REP1_WT/scenicplus/scplus_obj.pkl"

with open(path, "rb") as f:
    scplus_obj = pickle.load(f)

tf2g = scplus_obj.uns["TF2G_adj"]
r2g = scplus_obj.uns["region_to_gene"]
cistromes = scplus_obj.uns["Cistromes"]["Unfiltered"]

tf2r_rows = []
for key, pyranges_obj in cistromes.items():
    df = pyranges_obj.df
    tf_name = key.split("_(")[0]
    df["Region"] = (
        df["Chromosome"].astype(str)
        + ":"
        + df["Start"].astype(str)
        + "-"
        + df["End"].astype(str)
    )
    for region in df["Region"]:
        tf2r_rows.append([tf_name, region])

tf2r = pd.DataFrame(tf2r_rows, columns=["TF", "Region"])


tf2g.to_csv("../Results/REP1_WT_TF2G.csv", index = False)
r2g.to_csv("../Results/REP1_WT_R2G.csv", index = False)
tf2r.to_csv("../Results/REP1_WT_TF2R.csv", index = False)


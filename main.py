import numpy as np
import pandas as pd

##

racine="/Users/yassinhamaoui/RL-crypto/"
fenetre=50

data=pd.read_csv(racine+"XETHZEUR_complete_candle_15min.csv")

price=data[["candle_15min","P_close"]]
price=price.rename(index=str,columns={"P_close":"eth"})
price["euros"]=1
price=price.set_index("candle_15min")
price=price[["euros","eth"]]
price["eth"]=price["eth"].pct_change()+1
y=price






import numpy as np
import pandas as pd

##

#change racine
racine="/Users/yassinhamaoui/RL-crypto/"
fenetre=50

#get the data
data=pd.read_csv(racine+"XETHZEUR_complete_candle_15min.csv")


#Reorganize the data
price=data[["candle_15min","P_close"]]
price=price.rename(index=str,columns={"P_close":"eth"})
price=price.set_index("candle_15min")
data=data.set_index(price.index)
price["eth"]=price["eth"].pct_change()+1
for i in range(fenetre):
price["t-{}".format(i)]=data.P_close.shift(i)








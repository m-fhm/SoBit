import pandas as pd
df=pd.read_csv('mempool.csv')
df=df.sort_values(by = 'fee',ascending = False)
transactions=df.values.tolist()
try:
    out_data = open("block.txt",'a')# open block.txt file to write transations as output
    block_weight=0
    tracked_transactions= []
    for transaction in transactions:
        if block_weight <= 4000000:
            if type(transaction[3]) is not str: #check if the transation have parent or not transaction[3] pick the parents of transation
                out_data.write(transaction[0])
                out_data.write("\n")
                block_weight= block_weight + transaction[2] #calculate the block weight
            else:            
                transation_parents= transaction[3].split(';')
                check =  all(item in tracked_transactions  for item in transation_parents)
                if check is True:
                    out_data.write(transaction[0])
                    out_data.write("\n")
                    block_weight= block_weight + transaction[2] #calculate the block weight
except:
    print("generic error")
else:
    print("completed successfully ")
    out_data.close()

"""Parse weight and parents fields; What i understand is to write those transactions which have parents from mempool to block.txt """
def parse_mempool_csv():
    """Parse the CSV file and return a list of MempoolTransactions."""
    with open('mempool.csv') as mempool:
        return([line.strip().split(',') for line in mempool.readlines()])
try:
    transations = parse_mempool_csv()
    out_data = open("block.txt",'a')# open block.txt file to write transations as output
    block_weight=0
    for transation in  transations[1:]:
        if transation[3] !='': #check if the transation have parent or not transaction[3] pick the parents of transation
            block_weight= block_weight + int(transation[2]) #calculate the block weight
            if block_weight <= 4000000: 
                transation_parents= transation[3].split(';') #collect the parents in transation_parents list
            for item in transation_parents: #pick the parent from list of parents
                out_data.write("\n")
                out_data.write(item) #write the parent before transation 
            out_data.write("\n")  
            out_data.write(transation[0]) #write the transation at end of parents
except:
    print("generic error")
else:
    print("completed successfully ")
    out_data.close()

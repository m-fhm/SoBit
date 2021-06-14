"""Parse weight and parents fields."""
def parse_mempool_csv():
    """Parse the CSV file and return a list of MempoolTransactions."""
    with open('mempool.csv') as mempool:
        return([line.strip().split(',') for line in mempool.readlines()])
data = parse_mempool_csv()
out_data = open("block.txt",'a')
block_weight=0
for d in  data[1:]:
    if d[3] !='':
        block_weight= block_weight + int(d[2])
        if block_weight <= 4000000:
            de= d[3].split(';')
        for item in de:
            print(item)
            out_data.write("\n")
            out_data.write(item)
        out_data.write("\n")  
        out_data.write(d[0])
      
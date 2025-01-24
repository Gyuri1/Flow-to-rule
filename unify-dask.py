import dask.dataframe as dd
from dask.distributed import Client
import dask_expr
from multiprocessing import freeze_support
import sys

# Avoiding shuffle warning
import logging
logging.getLogger("distributed.shuffle").setLevel(logging.ERROR)

# main function
def unify_main(input_file, output_file):
    print("Reading data file:", input_file)
    connections_df = dd.read_csv(input_file) 
    print(connections_df.head())
   
    print("Processing data:")
    subset=['Subject IP Address', 'Peer IP Address', 'Peer Port/Protocol']
    fw_rules = connections_df.drop_duplicates(subset=subset).loc[:, subset]
    # Print Output
    fw_result=fw_rules.compute()
    print(fw_result.head())  # compute() will activate the dash 
    print("Writing firewall rules:", output_file)
    fw_result.to_csv(output_file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python unify-dash.py <input_netflow_csv_file> <output_csv_file>")
    else:
        print("dask_expr version:",dask_expr.__version__)
        freeze_support()
        # Dask client
        client = Client()       
        unify_main(sys.argv[1], sys.argv[2]) 
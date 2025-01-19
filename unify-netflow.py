import pandas as pd
import numpy as np
import sys

def unify_data(connections_df, fw_rules):
    # Aggregate connections between host groups
    subset=['Subject IP Address', 'Peer IP Address', 'Peer Port/Protocol']
    fw_rules = connections_df.drop_duplicates(subset=subset).loc[:, subset]
    return fw_rules

def unify_main(input_file, output_file):
    print("Reading data file:", input_file)
    connections_df = pd.read_csv(input_file, parse_dates=['Start']) 
    print(connections_df.head())

    print("Processing data:")
    fw_rules = pd.DataFrame({'Source', 'Destination', 'Peer Port/Protocol'})
    fw_rules = unify_data(connections_df, fw_rules)
    print(fw_rules.head())
    print("Writing firewall rules:", output_file)
    fw_rules.to_csv(output_file)

# main
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python unify-netflow.py <input_netflow_csv_file> <output_csv_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]       
        unify_main(input_file, output_file)     

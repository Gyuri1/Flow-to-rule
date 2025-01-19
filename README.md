# Flow to Rule 

This script converts network flow data into firewall rules. It filters based on the following fields: 'Subject IP Address', 'Peer IP Address', and 'Peer Port/Protocol'.

How to install:
====
To install and set up the script, follow these steps:  
	1.	Clone the repository to your local machine: ```git clone https://github.com/Gyuri1/Flow-to-rule```  
	2.	Navigate to the project directory: ```cd Flow-to-rule``` 
	3.	Ensure you have Python 3 installed. You can check your Python version with: ```python3 --version```  

How to run:
====
To convert flow data into firewall rules, run the following command:

    python3 unify-netflow.py netflow-large.csv firewall-rules.csv 


Expected Output: 
====

After running the script, you should obtain a CSV file named firewall-rules.csv containing the generated firewall rules.  

   ```sh
python3 unify-netflow.py netflow-large.csv firewall-rules.csv   
Reading data file: netflow-large.csv  
                      Start          Duration  ... Peer Bytes Actions  
0 2024-11-25 19:10:12+00:00  2d 2hr 32min 47s  ...     1.26 G     NaN  
1 2024-11-25 19:10:44+00:00  2d 2hr 32min 15s  ...   414.89 M     NaN  
2 2024-11-27 17:12:44+00:00     4hr 29min 30s  ...   172.65 M     NaN  
3 2024-11-27 21:20:03+00:00         22min 56s  ...    29.96 M     NaN  
4 2024-11-27 21:17:49+00:00         25min 10s  ...     1.02 M     NaN  
  
[5 rows x 13 columns]  
Processing data:  
  Subject IP Address Peer IP Address Peer Port/Protocol  
0        10.201.3.20     10.201.1.51          22609/TCP  
1        10.201.3.21    10.203.0.212            443/TCP  
2        10.201.3.21    10.203.0.202            443/TCP  
3       10.202.3.111    10.10.101.99            445/TCP  
4       10.201.1.239    10.202.1.231             22/TCP  
Writing firewall rules: firewall-rules.csv
 ```

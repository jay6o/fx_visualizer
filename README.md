# Market Data Visualization  

This program gets data using the Oanda brokerages API, processes it using pandas, and visualises it through mplfinance. The data is visualized from 2010-2024 in monthly granularity for the GBPJPY foreign exchange pair.

## Samples
#### Chart
![image](https://github.com/user-attachments/assets/173b9438-6994-430e-9a9f-3443680f42cc)
#### JSON data from the brokerages API
<img width="587" alt="Screenshot 2024-08-02 at 5 16 37 PM" src="https://github.com/user-attachments/assets/a5248305-9617-4c81-b374-b981658889f9">



## Usage:
If you plan on using this program you must get your own API key from Oanda & create an env file that matches up with the variables used in the existing program.
You can also just hardcode your personal information if you don't plan on sharing it.   

  

- #### Clone the repo to your machine
  
- `git clone <this_repo_URL>`  


- #### Install Python dependencies using the requirements.txt provided

- `cd /path/to/repo`

- `pip install -r requirements.txt`

- #### Run the program

- `python3 main.py`

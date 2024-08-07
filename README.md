# Foreign Exchange Market Visualizer 

This program gets data using the Oanda brokerages API, processes it using pandas, and visualises it through mplfinance. The client is able to select from a large variety of exchange pairs, granularities and ranges of data (time) using the CLI menu.

## Samples
#### Chart
![image](https://github.com/user-attachments/assets/173b9438-6994-430e-9a9f-3443680f42cc)

#### JSON data from the brokerages API
<img width="587" alt="Screenshot 2024-08-02 at 5 16 37 PM" src="https://github.com/user-attachments/assets/a5248305-9617-4c81-b374-b981658889f9">

#### Menu
<img width="360" alt="Screenshot 2024-08-07 at 6 50 33 PM" src="https://github.com/user-attachments/assets/fd6dec0c-03f7-40a8-9539-3678c6ff7ef9">\
<img width="250" alt="Screenshot 2024-08-07 at 6 51 28 PM" src="https://github.com/user-attachments/assets/7ac17628-9597-487e-8af2-ef8f8f226853">\
<img width="184" alt="Screenshot 2024-08-07 at 6 51 46 PM" src="https://github.com/user-attachments/assets/e32a20a5-8515-40b3-9866-c68ee71614cf">


## Usage:
If you plan on using this program you must get your own API key from Oanda & enter your information into the `env.template` provided in `/modules`.
You can also just hardcode your personal information if you don't plan on sharing it.   

  

- #### Clone the repo to your machine
  
- `git clone <this_repo_URL>`  


- #### Install Python dependencies using the requirements.txt provided

- `cd /path/to/repo`

- `pip install -r requirements.txt`

- #### Run the program

- `python3 main.py`

import pandas as pd

customer_dataset1 = {
    'Bank ID': ['1', '2', '3', '4', '5'],
    'First Name': ['Greg', 'Shelly', 'Raymond', 'Ignacio', 'Hector'],
    'Last Name': ['Smith', 'Schultz', 'Cabrera', 'Yelich', 'Chourio']
}

customer_dataset2 = {
    'Bank ID': ['6', '7', '8', '9', '10'],
    'First Name': ['Preston', 'Jamal', 'Kenny', 'Axel', 'Cherie'],
    'Last Name': ['White', 'Murray', 'Smith', 'Reese', 'Fogel']
}

salary_dataset = {
    'Annual Salary': [97000, 65000, 104000, 55000, 27000, 68000, 165000, 32000, 62000, 14000]
}

Bank_df_1 = pd.DataFrame(customer_dataset1, columns=['Bank ID', 'First Name', 'Last Name'])
Bank_df_2 = pd.DataFrame(customer_dataset2, columns=['Bank ID', 'First Name', 'Last Name'])
salary_df = pd.DataFrame(salary_dataset)

bank_df_all = pd.concat([Bank_df_1, Bank_df_2], ignore_index=True)
bank_df_all['Annual Salary'] = salary_df['Annual Salary']
bank_df_all 

new_client_dataset = {
    'Bank ID': 11,
    'First Name': 'Owen',
    'Last Name': 'Campbell',
    'Annual Salary': 30000
}

new_client_df = pd.DataFrame([new_client_dataset])

bank_df_all = pd.concat([bank_df_all, new_client_df], ignore_index=True)
bank_df_all
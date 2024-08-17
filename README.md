# PROJECT NAME: Bank Client Data Management

## OVERVIEW
This project involves managing and analyzing bank client data using Python's Pandas library. The tasks include creating and merging dataframes, adding new client information, and integrating salary data for a complete view of the bank's clients.

## TABLE OF CONTENTS
1. Installation
2. Usage
3. Features
4. Documentation
5. Credits

## INSTALLATION 

### Prerequisites
- Python 3.10.9 (this is the version used for development and testing)
- Third-party libraries: `pandas`

### Steps
1. Clone the repository:
    git clone https://github.com/ocampbell378/BankClientDataManagement.git
2. Install the required libraries:
    pip install -r requirements.txt

## USAGE
To run the project, use the following command:
python main.py

## FEATURES
- **Feature 1**: Define a dataframe named `Bank_df_1` containing the first and last names of 5 bank clients.
- **Feature 2**: Create another dataframe `Bank_df_2` with information about 5 new clients.
- **Feature 3**: Concatenate the two dataframes (`Bank_df_1` and `Bank_df_2`) to form a unified dataframe.
- **Feature 4**: Merge the client names with their salary information using the `Bank Client ID`.
- **Feature 5**: Add your own client information to the dataset and update the dataframe.

## DOCUMENTATION
### Modules and Functions
- **main.py**: Contains the primary logic for processing and manipulating the bank client data.
  - `create_dataframe()`: Defines and returns a dataframe with client information.
  - `concatenate_dataframes()`: Concatenates two dataframes into one.
  - `merge_dataframes()`: Merges client data with their corresponding salary information.
  - `add_new_client()`: Adds a new client to the existing dataframe.

## CREDITS
- Developed by Owen Campbell
- This project came from the Python for Data Analysis: Pandas & NumPy guided project by Ryan Ahmed on Coursera.

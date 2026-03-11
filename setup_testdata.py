import pandas as pd
import os

def create_excel():

    if not os.path.exists("testdata"):
        os.makedirs("testdata")

    # The test data to inject
    data = {
        "username": ["demouser"],
        "password": ["testingisfun99"],
        "product": ["iPhone 12"],
        "fname": ["Sushant"],
        "lname": ["Automation"],
        "address": ["bhubaneshwar"],
        "state": ["Odisha"],
        "zip": [751024]
    }


    df = pd.DataFrame(data)
    df.to_excel("testdata/testdata.xlsx", index=False)
    print("Success! 'testdata.xlsx' has been generated in the 'testdata' folder.")

if __name__ == "__main__":
    create_excel()
import requests
from time import time

times = int(input("Enter the number of times you want the API tested: "))

with open('test_docs/api_test.txt', 'r+') as file:
    file.truncate(0)
    for i in range(1,times+1):
        start = time()
        x = requests.get('http://127.0.0.1:5000/')
        end = time()
        file.write(f"Test Number: {i}\n")
        file.write(f"Status Code: {x}\n")
        file.write(f"Time (s): {end-start}\n\n")




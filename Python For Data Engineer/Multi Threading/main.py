import time
import random
from concurrent.futures import ThreadPoolExecutor

tables = ["Orders", "Products", "Customers", "Reviews", "Cancle"]

def my_func(i):

    wait = random.randint(1, 10)
    time.sleep(wait)
    print(f"{i} tooks {wait} sec for execute...")

with ThreadPoolExecutor(max_workers=len(tables)) as executor:
    futures = executor.map(my_func, tables)
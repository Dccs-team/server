import requests
from concurrent.futures import ThreadPoolExecutor

def make_request(url):
    with requests.Session() as ses:
        response = ses.get(url)
        print('Done')

if __name__ == "__main__":
    urls = ['https://camo.githubusercontent.com/5fe4c339179e986bbc91d54cbda95cc20472a740bc07d1ce4c7ebd1a8589cfac' for _ in range(10000)]

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(make_request, urls)

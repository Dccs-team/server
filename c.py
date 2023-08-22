import requests
from concurrent.futures import ThreadPoolExecutor

def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses
        print("Request to", url, "is done")
    except requests.RequestException as e:
        print("Request to", url, "failed:", e)

if __name__ == "__main__":
    urls = ['https://camo.githubusercontent.com/26a5a007ec201d8120179ce042c538274f11c0da3c6909c83eaf79547b2186a1/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d646363732d7465616d' for _ in range(10000)]

    with ThreadPoolExecutor(max_workers=200) as executor:
        executor.map(make_request, urls)

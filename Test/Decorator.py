def timing(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('The function has been working for {} seconds' .format(end - start))
        return return_value
    return wrapper

@timing
def get_request(url):
    import requests
    req = requests.get(url)
    return req.text

@timing
def func(x):
    import time
    time.sleep(x)
    
if __name__ == "__main__":
    print(get_request('https://google.com'))

    

import requests
from bs4 import BeautifulSoup

def get_content():
    url = "https://www.wsj.com/tech/ai"
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    response = requests.get(url, headers=header)

    print(f'The status is: {response}')

    if response.status.code==200:
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')

        for p in paragraphs:
            print(p.get('class', []))


if __name__=="__main__":
    print("running")
    get_content()

from bs4 import BeautifulSoup
import requests


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.ok:
        return r.text
    else:
        print(r.status_code)


def get_seans_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find_all('tr')
    seasons = []
    i = 6
    for td in trs:
        try:
            season = trs[i].text.strip().replace('\n', ' ')
            if 'руб' not in season:
                break
            # print(season)
            seasons.append(season)
            i += 2
        except:
            break



    return seasons


def main():
    url = 'http://penza-afisha.ru/seans.php?film=3742'
    html = get_html(url)

    dict_data = {
        'Расписание': get_seans_data(html)
    }

    print(dict_data)


if __name__ == '__main__':
    main()

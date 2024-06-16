"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        nums = soup.tbody.find_all('tr')
        male_num = 0
        female_num = 0
        for num in nums[:-1]:
            n = num.text

            if len(n) != 1:
                info_list = n.split(' ')
                male_num += int(info_list[1].replace(',', ''))
                female_num += int(info_list[3].replace(',', ''))
        print(f'Male Number: {male_num}')
        print(f'Female Number: {female_num}')






if __name__ == '__main__':
    main()

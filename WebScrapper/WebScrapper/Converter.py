from bs4 import BeautifulSoup  
import numpy as np

mega_Array = []

for i in range (1,99):
    with open('2023/{i}.html'.format(i=str(i)), 'r', encoding='UTF-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    rowgroups = soup.find_all("div", class_="rowgroup")

    hrefs = []
    texts = []

    for rowgroup in rowgroups:
        anchor_tags = rowgroup.find_all("a")
        hrefs .append([anchor_tag["href"] for anchor_tag in anchor_tags][0])

        div = rowgroup.find("div", class_="col-sm-9 col-lg-10")
        text = div.get_text()
        texts .append(text.strip())
    
    filtered_hrefs = []

    for href in hrefs:
            filtered_hrefs.append(href.replace('/2023', '').replace('/',''))

    combined_array = []
    for i2 in range(len(texts)):
        mega_Array.append([filtered_hrefs[i2], texts[i2]])
   
    print(i)


array = np.array(mega_Array)
np.savetxt("array.csv", array, delimiter=";", fmt="%s")
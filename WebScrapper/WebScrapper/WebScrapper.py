#Seite ZTF

import requests

for count_Site in range(27,99):
    
    if(count_Site <=9):
        response = requests.get('https://www.zolltarifnummern.de/2023/0'+str(count_Site))
    else:
        response = requests.get('https://www.zolltarifnummern.de/2023/'+str(count_Site))


    if response.status_code == 200:
        # The download was successful
        with open('2023/{count_Site}.html'.format(count_Site=str(count_Site)), 'wb') as f:   
            f.write(response.content)
    else:
        # The download failed
        raise Exception('Failed to download HTML file')
    print(count_Site)



    #for x in range(1, 99):

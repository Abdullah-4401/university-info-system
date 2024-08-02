import requests
from app.university.models import UniData

class UniversityDataHandler:
    APIURL='http://universities.hipolabs.com/search?country=United+Kingdom'
    @classmethod
    def fetch_data(call):
        response = requests.get(call.APIURL)
        if response.status_code==200:
            return response.json()
        else:
            raise Exception('Fail to fetch data')

    @classmethod
    def fetch_and_store_data(call):
        data=call.fetch_data()
        for i in data:
            UniData.objects.update_or_create(
                name=i['name'],
                defaults={
                    'web_pages': i['web_pages'],
                    'country':i['country'],
                    'state_province': i.get('state-province',''),
                    'domains':i['domains'],
                    'alpha_two_code':i['alpha_two_code'],
                },
            )

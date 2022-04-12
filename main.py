import requests

url = 'https://graphql.anilist.co/'

query = '''
query ($id: Int) { # Define which variables will be used in the query (id)
  Media (id: $id, type: MANGA) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
    id
    title {
      romaji
      english
      native
    }
    status
    startDate{
        year
    }
    endDate {
        year
    }
    genres
    
  }
}
'''

variables = {
    'id': 30001
}

response = requests.post(url, json={'query': query, 'variables': variables})
json_response = response.json()

print(json_response)
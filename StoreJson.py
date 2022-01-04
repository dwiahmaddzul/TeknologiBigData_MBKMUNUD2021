import pandas as pd
import pymongo

df = pd.read_json('Json File/Wargatiktok.json',lines=True)

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['dbtweets']
mycol = mydb['dtweet']

data = df.to_dict('records')

cursor = mycol.find(fields=['content'])
tweet_fields = ['content']
result = pd.DataFrame(list(cursor), columns = tweet_fields)

print(result[2])

#print(data[0])

# insert
mycol.insert_many(data)
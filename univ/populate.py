from .models import *
import pandas as pd
def populate_univ():
    df=pd.read_csv('C:/Projects/we code/core/project/univ/univs.csv',encoding='cp1252')
    for _,row in df.iterrows():
        univs.objects.create(
            name=row['name'],
            img=row['image_url'],
            location=row['location'],
            acceptance=row['Acceptance'],
            gre=row['GRE']
        )

def populate_ranks():
    df=pd.read_csv('C:/Projects/we code/core/project/univ/rankings.csv',encoding='cp1252')
    for _, row in df.iterrows():
        try:
            university = univs.objects.get(name=row['name'])
            ranks.objects.update_or_create(
                name=university,
                defaults={
                    'country': row['Country'],
                    'topic': row['Topic'],
                    'score': row['Score']
                }
            )
        except univs.DoesNotExist:
            print(f"University '{row['name']}' not found. Skipping this entry.")
#C:/Projects/we code/core/project/univ/populate.py
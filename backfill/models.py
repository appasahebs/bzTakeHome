from django.db import models
import pandas as pd
from articles.models import Article

# Create your models here.


class Backfill(models.Model):

    # This method is for import test data from csv file to database
    def populate():
        df = pd.read_csv('./benzinga_articles.csv', sep=',')
        for i in range(len(df)):
            a = Article(
                url=df.iloc[i][0],
                title=df.iloc[i][1],
                publish_date=df.iloc[i][2],
                authors=df.iloc[i][3],
                section=df.iloc[i][4],
                tags=df.iloc[i][5],
                sort=df.iloc[i][6])
            a.save()

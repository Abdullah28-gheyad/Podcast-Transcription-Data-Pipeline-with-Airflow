# Dag for --> how to define our pipeline
# Task --> How to define each individual task
# pendulum for time
from airflow.decorators import dag , task
import pendulum
import requests
import xmltodict
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.sqlite.hooks.sqlite import SqliteHook
import os
@dag(
    dag_id= 'podcast_summary2',
    schedule='@daily',
    start_date = pendulum.datetime(2023,10,9)
)

# initialize data pipeline
def podcast_summary2():
    
    create_database = SqliteOperator(
        task_id = "create_table_sqlite",
        sql = r"""
            CREATE TABLE IF NOT EXISTS episodes(
            link TEXT PRIMARY KEY, 
            title TEXT,  
            fileName TEXT , 
            published TEXT, 
            description TEXT 
            )
            """ ,
            sqlite_conn_id="podcasts"
    )

    @task
    def get_episodes():
        data = requests.get("https://www.marketplace.org/feed/podcast/marketplace/")
        feed = xmltodict.parse(data.text)
        episodes = feed["rss"]["channel"]["item"]
        print(len(episodes))
        return episodes
    
    prodcast_epispdes = get_episodes()
    create_database.set_downstream(prodcast_epispdes)   




    @task
    def load_episodes(episodes):
        hook = SqliteHook(sqlite_conn_id = "podcasts")
        stored = hook.get_pandas_df("SELECT * FROM episodes")
        new_episodes = []
        for episode in episodes:
            if episode["link"] not in stored["link"].values:
                filename = f"{episode['link'].split('/')[-1]}.mp3"
                new_episodes.append([episode["link"] , episode["title"] , episode["pubDate"] , episode["description"] , filename])
        hook.insert_rows(table="episodes" , rows=new_episodes , target_fields=["link","title","published","description","fileName"])
    
    load_episodes(prodcast_epispdes)



    @task()
    def download_episodes(episodes):
        for episode in episodes:
            filename = f"{episode['link'].split('/')[-1]}.mp3"
            audio_path = os.path.join("episodes" , filename)
            if not os.path.exists(audio_path):
                print(f"Downloading {filename}")
                audio = requests.get(episode["enclosure"]['@url'])
                with open(audio_path , "wb+") as f:
                    f.write(audio.content)
    
    download_episodes(prodcast_epispdes)
    
summary = podcast_summary2()



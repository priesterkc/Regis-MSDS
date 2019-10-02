import requests
import pandas as pd

"""
This function takes in a list that is passed back from the website JSON response
and a list of the keys to call when collecting the data. Each value for a key for
every post will be stored into the column for a dataframe. The resulting dataframe
will be returned back to the getData function. This dataframe is the posts that
are collected for up to 25 posts in the specified time range in the getData function.
"""
def extractData(posts_ls, key_ls):

    small_df = pd.DataFrame()

    for key in key_ls:

        #list to hold values
        data_ls=[]

        for post in posts_ls:

            try:
                data_ls.append(post[key])
            except:
                data_ls.append(None)

        small_df[key] = data_ls

    return small_df

"""
This function takes in the parameters for the start to end datetime range to collect
the data, in addition to the list of JSON structure keys and subreddit to collect the data
from. The function will use the PushShift API to access Reddit and proceed with collecting
data if the connection to the website is successful.
"""

def getData(after, before, keys, sub):

    df = pd.DataFrame()

    while before > after:

        #get posts between dates & for subreddit
        url = r'https://api.pushshift.io/reddit/search/submission/?before=' \
                +str(before)+'&after='+str(after)+'&subreddit='+sub

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()['data']

            exData_df = extractData(data, keys)

            #if length is 0, stop loop b/c nothing more was posted
            if len(exData_df) == 0: break

            else:
                after = exData_df['created_utc'].iloc[-1]

                df = df.append(exData_df, ignore_index=True)

        else:
            print('The connection was not successful.')
            break

    print(f'Finished collecting data from r/{sub}; there are {len(df)} posts.')

    return df


#Unix Epoch timestamp
start_date = 1554681600 #2019-04-08
end_date = 1555200000   #2019-04-14

#keys to collect data from
post_keys = ['id', 'created_utc', 'author', 'can_mod_post', 'link_flair_text',
            'title', 'num_comments', 'score', 'permalink']

#run the getData function on the r/datascience subreddit
DS_posts_df = getData(start_date, end_date, post_keys, 'datascience')

#put data in csv file
DS_posts_df.to_csv("datafrom_r_datascience.csv", index=False)
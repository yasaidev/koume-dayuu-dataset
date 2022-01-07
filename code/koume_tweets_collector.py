import twint
import pandas as pd


def twint_get_user(user_name, limit):
    c = twint.Config()
    c.Username = user_name
    c.Limit = limit
    c.Store_csv = True
    c.Store_object = True
    c.Output = f"../data/{user_name}.csv"
    c.Resume = f"../data/{user_name}_resume"
    c.Pandas = True

    twint.run.Search(c)


if __name__ == "__main__":
    user_name = "dayukoume"
    limit = 5000
    twint_get_user(user_name, limit)
    koume_tweets_df = pd.DataFrame(twint.storage.panda.Tweets_df)
    print(koume_tweets_df)

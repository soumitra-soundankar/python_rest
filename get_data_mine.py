import pandas as pd
import mysql.connector

def get_intra_day():
    db = mysql.connector.connect( host = "host",
                            user = "user",
                            passwd = "password",
                            db = "d")
    sql = "select * from t_quotes where date(create_date) = '2021-04-12'" # TODO: need to pass timeframe
    df = pd.read_sql(sql, con=db)
    return df

def get_pre_open_day():
    db = mysql.connector.connect( host = "host",
                            user = "user",
                            passwd = "password",
                            db = "db")
    sql = "select * from t_pre_open_market"
    df = pd.read_sql(sql, con=db)
    return df
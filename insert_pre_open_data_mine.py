import pandas as pd
import mysql.connector

def insert_portfolio(market_data):
    db = mysql.connector.connect( host = "remotemysql.com",
                            user = "RUFDjh411O",
                            passwd = "Wouc0W9yZu",
                            db = "RUFDjh411O")
    cursor = db.cursor()

    sql = "delete from t_pre_open_market"
    cursor.execute(sql)
    db.commit()

    sql = "INSERT INTO t_pre_open_market(exchange, ticker,identifier,last_price,changed_value,percent_change,previous_close, last_update_time) " \
          "VALUES('NSE', %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(sql, market_data)
    cursor.close()
    db.commit()


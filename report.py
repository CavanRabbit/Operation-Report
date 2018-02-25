import pymysql
import urllib, json, traceback, datetime, sys, time, os, logging
import logging.handlers

#数据库配置信息
hostname = ''
port = 8501
dbname = ''
username = ''
password = ''

conn = None

#get数据库连接
def get_conn():
    try:
        conn = pymysql.connect(host=hostname, port = port, user = username, passwd = password, db=dbname)
    except Exception as e:
        print(e)
        return None

    return conn



def get_metric_data(metric_id, start_time, end_time, value_type, time_type):


    if(value_type==0):
        value_string = 'metric_value'
    elif value_type==1:
        value_string = 'max(metric_value)'
    elif value_type==2:
        value_string = 'avg(metric_value)'
    else:
        print('The value of valueType is wrong')
        return None

    if time_type==0:
        sql = 'select %s from metric_daily_data where metric_id=%d and ' \
              'collect_time>%d and collect_time<%d ' \
              'order by collect_time desc' % (value_string,metric_id, start_time, end_time)
    elif time_type==1:
        sql = 'select %s from metric_daily_data where metric_id=%d and ' \
              'collect_time>unix_timestamp(%s) and collect_time<unix_timestamp(%s) ' \
              'order by collect_time desc' % (value_string, metric_id, start_time, end_time)
    else:
        print('The value of time_type is wrong')
        return None

    result = None
    cursor = None
    if conn is None:
        print('Can not get any db connections')
        return None
    try:
        cursor = conn.cursor()
        result_set = cursor.execute(sql)
        return result_set
    except Exception as e:
        print(e)
        return None
    finally:
        cursor.close()



def get_sum_data(metric_id, start_time, end_time, value_type, time_type):

    conn = get_conn()
    result_set = get_metric_data(metric_id, start_time, end_time, value_type, time_type)
    result = result_set[0][0]
    conn.close()








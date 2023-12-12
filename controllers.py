from init_db import get_db_connection
from helpers import to_dict,list_dict
import json


def all_logs():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM logs;')
    logs = list_dict(cur.fetchall())
    cur.close()
    conn.close()


    return logs

def new_log(ip_address: str,
         request_url: str,
         request_path: str,
         request_method: str,
         request_time: str,):

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO logs (ip_address, request_url, request_path, request_method, request_time)'
                    'VALUES (%s, %s, %s,%s, %s) RETURNING *;',(ip_address,
                                                    request_url,
                                                    request_path,
                                                    request_method,
                                                    request_time,
                                                    ))

    log = cur.fetchone()[:]
    log_dict = to_dict(log)
    conn.commit()
    cur.close()
    conn.close()

    return json.dumps(log_dict)

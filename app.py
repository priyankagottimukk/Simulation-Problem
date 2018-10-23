from flask import Flask, request, jsonify
from db_ops import sqlite_conn
app = Flask(__name__)


import uuid, time
@app.route("/chat", methods=["POST"])
def insert_chats():
    conn = sqlite_conn()
    try:
        di = request.get_json()
        id = str(uuid.uuid4()).split("-")[0]
        values_li = ["'%s'" %id, "'%s'" %di["username"], "'%s'" %di["text"], "'%s'" %(int(time.time())),  "'%s'" %(di.get("timeout", "60")) ]
        resp = conn.insert_row("chats", values_li)
        if not resp:
            raise
        resp = jsonify({"id": id})
        resp.status_code = 201
        return resp
    except Exception as e:
        print(e)
        return "API Failed :("
    finally:
        conn.close_conn()

@app.route("/chat/<id>", methods=["GET"])
def get_chat_by_id(id):
    conn = sqlite_conn()
    try:
        where_clause = "%s='%s'" %("id", id)
        #expect one tuple
        li = conn.get_data("chats", where_clause)
        if not li:
            return jsonify()
        li = li[0]
        epoch_expiry = (int(li[3]) + int(li[4]))
        expiry_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_expiry))
        return jsonify({
            "username": li[1],
            "text": li[2],
            "expiration_date": expiry_time
        })

    except Exception as e:
        print(e)
        return "API Failed"    
    finally:
        conn.close_conn()

@app.route("/chats/<uname>", methods=["GET"])
def get_chat_by_uname(uname):
    conn = sqlite_conn()
    try:
        where_clause = "%s='%s'" %("username", uname)
        #expect list of tuple
        li = conn.get_data("chats", where_clause)
        json_list = []
        for rec in li:
            json_list.append({
                "id": rec[0],
                "text": rec[2]
            })
        return jsonify(json_list)

    except Exception as e:
        print(e)
        return "API Failed"    
    finally:
        conn.close_conn() 

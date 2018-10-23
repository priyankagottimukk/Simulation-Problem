from db_ops import sqlite_conn

conn_obj = sqlite_conn()
chats_table_status = conn_obj.create_table("chats", ["id", "username", "message", "time_created", "timeout"])
print("creating chats sqlite table status: %s" %chats_table_status)
if not chats_table_status:
    raise s
import sqlite3
from kafka import KafkaConsumer
from consumerAPI import kafkaconsumer


class SubService:

    def subscribe(sid, eid):
        conn = sqlite3.connect('pubsub.db')
        c = conn.cursor()
        c.execute("SELECT sid FROM subscriber WHERE sid = ? AND eid = ?", (sid, eid))
        val = c.fetchone()
        if val:
            c.execute("UPDATE subscriber SET subscription = 1 WHERE sid = ? AND eid = ?", (sid, eid))
        else:
            c.execute("INSERT INTO subscriber VALUES(?,?,?,?)", (sid, eid, 1, 0))
        conn.commit()
        conn.close()
        return

    def unsubscribe(sid, eid):
        conn = sqlite3.connect('pubsub.db')
        c = conn.cursor()
        c.execute("SELECT sid FROM subscriber WHERE sid = ? AND eid = ?", (sid, eid))
        val = c.fetchone()
        if val:
            c.execute("UPDATE subscriber SET subscription = 0 WHERE sid = ? AND eid = ?", (sid, eid))
        else:
            c.execute("INSERT INTO subscriber VALUES(?,?,?,?)", (sid, eid, 0, 0))
        conn.commit()
        conn.close()
        return

    # def view(sid, eid):
    #     conn = sqlite3.connect('pubsub.db')
    #     c = conn.cursor()
    #     c.execute("SELECT * FROM subscriber WHERE sid = ? AND eid = ? AND subscription = 1", (sid, eid,))
    #     val = c.fetchone()
    #     if val:
    #         updates = kafkaconsumer(eid)
    #     else:
    #         updates = 'Not subscribed !'
    #     return updates

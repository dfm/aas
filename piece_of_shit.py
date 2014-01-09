#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

__all__ = []

import json
import sqlite3


if __name__ == "__main__":
    with open("aas/abstracts.json") as f:
        data = json.load(f)

    with sqlite3.connect("aas/aas.db") as conn:
        c = conn.cursor()
        for doc in data:
            # session id.
            c.execute("select id from sessions where aas_id=?",
                      (doc["session_id"], ))
            session_id = c.fetchone()
            if session_id is None:
                c.execute("""insert into sessions(aas_id,title,date,room)
                             values(?,?,?,?)
                          """, (doc["session_id"], None, doc["date"],
                                doc["room"]))
                conn.commit()
                c.execute("select id from sessions where aas_id=?",
                          (doc["session_id"], ))
                session_id = c.fetchone()
            session_id = session_id[0]

            # abstract.
            c.execute("""insert into abstracts(aas_id,session_id,title,
                                               abstract,counts)
                            values(?,?,?,?,?)
                        """, (doc["id"], session_id, doc["title"],
                              doc["abstract"], json.dumps(doc["counts"])))
            conn.commit()
            c.execute("select id from abstracts where aas_id=?", (doc["id"], ))
            abstract_id = c.fetchone()[0]

            # authors.
            c.executemany("insert into authors(abstract_id,name) values(?,?)",
                          [(abstract_id, author) for author in doc["authors"]])

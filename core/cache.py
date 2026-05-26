import sqlite3,json,time,os,sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
def get_db():
    os.makedirs(os.path.dirname(config.DATABASE_PATH),exist_ok=True)
        conn=sqlite3.connect(config.DATABASE_PATH)
            conn.row_factory=sqlite3.Row
                return conn
                def setup_database():
                    conn=get_db()
                        c=conn.cursor()
                            c.execute("CREATE TABLE IF NOT EXISTS searches (id INTEGER PRIMARY KEY AUTOINCREMENT,search_query TEXT NOT NULL,category TEXT,results_json TEXT NOT NULL,alternatives_json TEXT,created_at REAL NOT NULL)")
                                c.execute("CREATE TABLE IF NOT EXISTS price_history (id INTEGER PRIMARY KEY AUTOINCREMENT,product_name TEXT NOT NULL,site TEXT NOT NULL,price REAL NOT NULL,recorded_at REAL NOT NULL)")
                                    conn.commit()
                                        conn.close()
                                        def save_search_results(query,results,alternatives,category="all"):
                                            conn=get_db()
                                                c=conn.cursor()
                                                    c.execute("DELETE FROM searches WHERE search_query=? AND category=?",(query.lower().strip(),category))
                                                        c.execute("INSERT INTO searches (search_query,category,results_json,alternatives_json,created_at) VALUES (?,?,?,?,?)",(query.lower().strip(),category,json.dumps(results),json.dumps(alternatives),time.time()))
                                                            for r in results:
                                                                    if r.get('price',0)>0:
                                                                                c.execute("INSERT INTO price_history (product_name,site,price,recorded_at) VALUES (?,?,?,?)",(r.get('name',query),r.get('site',''),r.get('price',0),time.time()))
                                                                                    conn.commit()
                                                                                        conn.close()
                                                                                        def get_cached_results(query,category="all"):
                                                                                            conn=get_db()
                                                                                                c=conn.cursor()
                                                                                                    expiry=time.time()-(config.CACHE_MINUTES*60)
                                                                                                        c.execute("SELECT results_json,alternatives_json,created_at FROM searches WHERE search_query=? AND category=? AND created_at>? ORDER BY created_at DESC LIMIT 1",(query.lower().strip(),category,expiry))
                                                                                                            row=c.fetchone()
                                                                                                                conn.close()
                                                                                                                    if row:
                                                                                                                            return {'results':json.loads(row['results_json']),'alternatives':json.loads(row['alternatives_json'] or '[]'),'cached':True,'cached_minutes_ago':int((time.time()-row['created_at'])/60)}
                                                                                                                                return None
                                                                                                                                def clear_expired_cache():
                                                                                                                                    conn=get_db()
                                                                                                                                        c=conn.cursor()
                                                                                                                                            c.execute("DELETE FROM searches WHERE created_at<?",(time.time()-(config.CACHE_MINUTES*60),))
                                                                                                                                                conn.commit()
                                                                                                                                                    conn.close()
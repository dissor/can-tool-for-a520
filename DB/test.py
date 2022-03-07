import sqlite3

# 创建与数据库的连接
conn = sqlite3.connect(':memory:')

# 创建一个游标
cur = conn.cursor()

# 建表的sql语句
sql_test_1 = '''CREATE TABLE scores (
    SN TEXT
)'''

# 执行sql语句
cur.execute(sql_test_1)

print("tishiiiii")

SN1, SN2 = "", ""
STATE_MN, STATE_CPUN, STATE_VMN, STATE_PN = "", "", "", ""
UUID = ""
OKEY = ""
USRKEY = ""
USRDATA = ""
MKEYA = ""
MKEYB = ""
MUSRDATA = ""
MUUID = ""
VMUUID = ""

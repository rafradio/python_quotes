import sys
import dbConnectSQL

def main(args):
    db = dbConnectSQL.DbConnectSQL()
    with open('users.txt') as f:
        data = [line.rstrip() for line in f]
        
    print(data)
    db.checkSQLUsers(data)

if __name__ == "__main__":
    main(sys.argv)
    
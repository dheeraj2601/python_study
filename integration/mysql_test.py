#!/usr/bin/python

import sys
import MySQLdb as mdb

# Open database connection
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'password'
DB_NAME = 'packetbroker'

def create_database():
    """
    Create a database table 
    """
    con = mdb.connect(DB_HOST, DB_USER, DB_PASSWORD)
    
    with con:
        cur = con.cursor()
        sql = "CREATE DATABASE IF NOT EXISTS "+ DB_NAME
        cur.execute(sql)

def mdb_get_version():
    """
    Get the mysql version using the MySQLdb. Compatible with Python DB API which
    makes the code more portable
    """
    con = None
    try:
        con = mdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    
        cur = con.cursor()
        cur.execute("SELECT VERSION()")
        data = cur.fetchone()
        print "Database version: %s" % data
        
    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)        
    finally:
        if con:
            con.close()


def create_and_populate(host_ip, remote_ip):
    """
    Create a table for writers and insert some data into it
    """
    con = mdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    
    with con:
        cur = con.cursor()
        sql = "CREATE TABLE IF NOT EXISTS `subscription` (`idsubscription` bigint(20) NOT NULL AUTO_INCREMENT, `destination` varchar(255)"    \
	      "NOT NULL, `offset` int(11) NOT NULL, `partitionnumber` int(11) NOT NULL, `priority` int(11) NOT NULL, `source`"  \
	      "varchar(255) NOT NULL, `topicname` varchar(255) NOT NULL, PRIMARY KEY (`idsubscription`)) "                      \
	      "ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1"
        cur.execute(sql)

	sql = None
	sql = "CREATE TABLE IF NOT EXISTS `venue` (`venue_id` bigint(20) NOT NULL AUTO_INCREMENT, `kafka_ip` varchar(255) NOT NULL, "         \
	      "`venue_name` varchar(255) DEFAULT NULL, PRIMARY KEY (`venue_id`), UNIQUE KEY `UK_8eve5kw195vgbu3fmv1k6bk0b` "    \
	      "(`venue_name`)) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1"

        cur.execute(sql)

        

        # insert some data

	sql = "INSERT INTO venue (kafka_ip, venue_name) VALUES('1.1.1.1:9092','ship')"
        cur.execute(sql)
    	con.commit()

	sql = "INSERT INTO venue (kafka_ip, venue_name) VALUES('1.1.1.2:9092','shore')"
        cur.execute(sql)
    	con.commit()

        
	sql = "INSERT INTO `packetbroker`.`subscription` (`destination`, `offset`, `partitionnumber`, "       \
	      "`priority`, `source`, `topicname`) VALUES ('shore', '0', '0', '30', 'ship', 'shore__chat__low')"
        cur.execute(sql)
    	con.commit()


	sql = "INSERT INTO `packetbroker`.`subscription` (`destination`, `offset`, `partitionnumber`, "       \
	      "`priority`, `source`, `topicname`) VALUES ('ship', '0', '0', '30', 'shore', 'ship__chat__low')"
        cur.execute(sql)
    	con.commit()

	sql = "INSERT INTO `packetbroker`.`subscription` (`destination`, `offset`, `partitionnumber`, "       \
              "`priority`, `source`, `topicname`) VALUES ('shore', '0', '0', '32', 'ship', 'shore__write__high')"
        cur.execute(sql)
    	con.commit()


	sql = "INSERT INTO `packetbroker`.`subscription` (`destination`, `offset`, `partitionnumber`, "       \
	      "`priority`, `source`, `topicname`) VALUES ('ship', '0', '0', '32', 'shore', 'ship__write__high')"
        cur.execute(sql)
    	con.commit()

 



        #for name in writers:
         #   cur.execute("INSERT INTO writers (NAME) VALUES ('%s')" % name)


def retrieve_data():
    """
    Retrieve the data from the table.
    """
    con = mdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    
    with con:
        cur = con.cursor()
        sql = "SELECT * FROM writers"
        cur.execute(sql)

        results = cur.fetchall()

        for r in results:
            print r



def retrieve_onebyone():
    """
    Retrieve data one row at a time instead of loading all results into memory at once
    """
    con = mdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    
    with con:
        cur = con.cursor()
        sql = "SELECT * FROM writers"
        cur.execute(sql)

        numrows = int(cur.rowcount)

        for i in range(numrows):
            row = cur.fetchone()
            print "%d %s"  % (row[0], row[1])

        print "There are %d total writers in all" % numrows


def dict_cursor():
    """
    Retrieving data using a dict cursor instead of the default tuple cursor
    """
    con = mdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    
    with con:
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM writers")

        results = cur.fetchall()

        for row in results:
            print "%d %s" % (row['id'], row['name'])

def with_description():
    """
    Retrieving the data and showing along with the column headers
    """
    con = mdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM writers")
        results = cur.fetchall()
        description = cur.description

        print description
        print "%s %s" % (description[0][0], description[1][0])

        for row in results:
            print "%d %s" % row

def update_prep_stmt():
    """
    Using prepared statements to update the entries
    """
    con = mdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

    with con:
        cur = con.cursor()
        cur.execute("UPDATE writers SET name = %s WHERE id = %s",
                    ('Guy de Muapasant', 4))

        print "Number of rows updated: %d" % cur.rowcount

def with_transactions():
    """
    Rollback if any of the queries result in an error
    Only supported by Innodb engine.
    Notice writer instead of writers in the 3rd query
    """
    try:
    	con = mdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    	
    	cur = con.cursor()    	
    	cur.execute("UPDATE writers SET name = %s WHERE id = %s",
    	            ("Leo Tolstroy", 1))
    	cur.execute("UPDATE writers SET name = %s WHERE id = %s",
    	            ("Boris Pasternak", 2))
    	cur.execute("UPDATE writer SET name = %s WHERE id = %s",
    	            ("Leonid Leoniv", 3))
    	
    	con.commit()
    	con.close()
    except mdb.Error, e:
        print 'Time to Rollback..'
        con.rollback()
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    
if __name__ == '__main__':
    create_database()
    mdb_get_version()
    create_and_populate()
    pass
    # retrieve_data()
    # retrieve_onebyone()
    # dict_cursor()
    # with_description()
    # update_prep_stmt()
    # with_transactions()

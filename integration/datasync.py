import MySQLdb
import sys
import os
import syslog
import fileinput
import subprocess
import time
import signal
import threading
from threading import Thread
from couchbase_test import_insert_bucket
import mysql_test as mt

def find_files(file_name):
    command = ['locate', file_name]
    output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]
    output = output.decode()
    return output

def stop_process(processname, processname_tag):
    pid = 0
    command = "ps ax | grep -i \' " + processname_tag + "\' | grep java | grep -v grep | grep -v '/bin/sh'" 
    for line in os.popen(command):
        fields = line.split()
        pid = fields[0]
        process = fields[4]
     
    if not pid :
        print "No " + processname + "server to stop"
    else:
        os.kill(int(pid), signal.SIGKILL)
    


def stop_processes():
    # stop sync manager

    #stop kafka
    stop_process('kafka', 'kafka\.Kafka')
    #stop zookeeper
    stop_process('zookeeper', 'QuorumPeerMain')
    #os.system('./bin/kafka-server-stop.sh')
    #os.system('./bin/zookeeper-server-stop.sh')

def start_processes():
    os.system('./bin/zookeeper-server-start.sh config/zookeeper.properties')
    sleep(2)
    os.system('./bin/kafka-server-start.sh config/server.properties')
    sleep(2)
    # locate sync-manager
    os.system('Java –jar sync-manager-webapp-0.15-1-SNAPSHOT.jar')
    sleep(2)

def change_config_files(host_ip2, remote_ip2):
    try:
        # change zookeeper property file
	for line in fileinput.input(['zookeeper.properties'], inplace=True):
            if line.strip().startswith('server='):
                count = 1
                line = str('server=' + host_ip2 + ':2888:3888\n')
            sys.stdout.write(line)
        sys.stdout.flush()
       
	if not count == 1:
            f = open(filename, 'a')
            f.write('server=' + host_ip2 + ':2888:3888' + '\n')
            f.close()

        # change kafka property file
	for line in fileinput.input(['server.properties'], inplace=True):
            if line.strip().startswith('host\.name='):
                count = 1
                line = str('host\.name=' + host_ip2 + '\n')
            sys.stdout.write(line)

            if line.strip().startswith('zookeeper.connect='):
                count = 1
                line = str('zookeeper.connect=' + host_ip2 + '\n')
            sys.stdout.write(line)
        sys.stdout.flush()

        if not count == 1:
            f = open(filename, 'a')
            f.write('port=9092\n')
            f.write('host\.name=' + host_ip2 + '\n')
            f.write('zookeeper.connect=' + host_ip2 + ':2181\n')
            f.close()
        
        # change data sync property file

    except IOError:
        print 'Problem reading: ' + filename

def _file(type_of, host_ip, remote_ip):
    try:
        filename = find_files('config/zookeeper.properties')
        path = os.path.dirname(filename)
        os.chdir(path)
        os.chdir('../')

        stop_processes()
 
        time.sleep(1)
        os.chdir('config')
        change_config_files(host_ip, remote_ip)
        os.chdir('../')

        start_processes()

	# couch base - create bucket and indexes
	_insert_bucket("write")
	_insert_bucket("chat")

	# mysql - create database . create tables and insert entries
	mt.create_database()
	if (type_of == "shore")
	mt.create_and_populate(host_ip, remote_ip)

    except IOError:
        print 'Problem reading: ' + filename

def _test():
    syslog.syslog(syslog.LOG_ERR, 'internal error')
    syslog.syslog(syslog.LOG_INFO, 'success')


if __name__ == '__main__':
    _file('shore', '10.10.10.10', '12.12.12.12')
    _test()

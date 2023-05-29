hadoop fs -mkdir -p  /data/
hadoop fs -copyFromLocal customers-hdfs.csv /data/
hadoop fs -ls /data/


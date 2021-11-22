# Hadoop Word Count Uni Project

## Copying code & input Files
```
docker cp src/ namenode:/home/
docker cp input.txt namenode:/home/

docker exec -it namenode bash -c 'hdfs dfs -mkdir -p input'
docker exec -it namenode bash -c 'hdfs dfs -put -f /home/input.txt input'
```

## Running MapReduce Job
```
docker exec -it namenode bash -c 'mapred streaming -files /home/src/mapper.py,/home/src/reducer.py -mapper mapper.py -reducer reducer.py -input input -output output'

docker exec -it namenode bash -c 'hdfs dfs -cat output/part-00000'
```

## Getting Output
```
docker exec -it namenode bash -c 'hdfs dfs -get -f output/part-00000 /home/output.txt'
docker cp namenode:/home/output.txt output.txt
```

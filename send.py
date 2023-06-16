from kafka import KafkaProducer
import json

def hello():

    value1={"name": "krishna"}


    # topic="demo1"
    producer = KafkaProducer(bootstrap_servers=['172.18.0.4:29092'], value_serializer = lambda x:json.dumps(x).encode('utf-8'))
    
    producer.send("from_rules_engine", value=value1)
    print("Message sent to Kafka topic")
    producer.flush()
     
hello()


# if __name__ =="__main__":
#         while 1 == 1:
#             val1=value
#             producer.send("demo1",val1)
            
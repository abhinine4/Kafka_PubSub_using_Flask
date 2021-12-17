from kafka import KafkaConsumer, TopicPartition


def kafkaconsumer(eid):
    bootstrap_servers = ['localhost:9092', 'localhost:9093', 'localhost:9094']
    if eid == 1:
        topicName = 'topic1'
    elif eid == 2:
        topicName = 'topic2'
    elif eid == 3:
        topicName = 'topic3'
    tp = TopicPartition(topicName, 0)
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, api_version=(2,0,2))
    # consumer.subscribe(topics)    #using assign() instead of subscribe()
    consumer.assign([tp])
    consumer.seek_to_beginning(tp)

    # obtain the last offset value
    lastOffset = consumer.end_offsets([tp])[tp]

    for message in consumer:
        updates = message.value.decode('utf-8')
        if message.offset == lastOffset - 1:
            break
    consumer.close()
    return updates


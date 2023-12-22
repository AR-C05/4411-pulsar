from pulsar import Admin

admin = Admin('pulsar://localhost:8080')
admin.topics().create_partitioned_topic(
    'persistent://public/default/my-partitioned-topic',
    4
)
admin.close()
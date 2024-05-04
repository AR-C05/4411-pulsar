# Apache Pulsar

tutorial for basic standalone cluster: https://pulsar.apache.org/docs/3.1.x/getting-started-standalone/  

## Pulsar installation:  
`wget https://archive.apache.org/dist/pulsar/pulsar-3.1.1/apache-pulsar-3.1.1-bin.tar.gz`  

Ensure the PulsarRootFolder path is correctly set in each of the shell scripts  
\- should point to the root folder of the unpacked Pulsar installation (without trailing slash)  

### Implementing/Running

Start a standalone cluster: `./startStandalone`  
\- stays on throughout  

if running for the first time, then create a topic  
\- \*\*\*note that the provided `Producer.py` and `Consumer.py` use the default topic created by `createTopicDefault`, and must be modified if topic created using `createTopicModular`  

start consumer using `startConsumer.sh`  
start producer using `startProducer.sh`  
(consumer and producer started in separate terminals)

----

MAIN branch:  
\- basic, no options  

PARTITIONS branch:  
\- requires a partition type topic explicitly created before use  
\- use `createPartitionedTopicModular.sh`  
\- has multiple consumers  

COMPRESSION branch:  
\- producer messages are compressed  

ACKNOWLEDGEMENT branch:  
\- NACKs on error  

BATCHING branch:  
\- producer sends messages in batches  

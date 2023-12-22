tenant=$1
namespace=$2
topic=$3
partitions=$4

PulsarRootFolder=~/apache-pulsar-3.1.1

$PulsarRootFolder/bin/pulsar-admin topics create-partitioned-topic persistent://$tenant/$namespace/$topic  --partitions $partitions

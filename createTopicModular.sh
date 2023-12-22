tenant=$1
namespace=$2
topic=$3

PulsarRootFolder=~/apache-pulsar-3.1.1

$PulsarRootFolder/bin/pulsar-admin topics create persistent://$tenant/$namespace/$topic

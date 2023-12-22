tenant=$1
namespace=$2
topic=$3

path=~/apache-pulsar-3.1.1

$path/bin/pulsar-admin topics create persistent://$tenant/$namespace/$topic

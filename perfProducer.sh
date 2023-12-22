PulsarRootFolder=~/apache-pulsar-3.1.1
$PulsarRootFolder/bin/pulsar-perf produce -s 1000 -r 10000 -u pulsar://localhost:6650 persistent://public/default/test-topic

PulsarRootFolder=~/apache-pulsar-3.1.1
$PulsarRootFolder/bin/pulsar-perf consume -n 1 -u pulsar://localhost:6650 -s test-sub persistent://public/default/test-topic

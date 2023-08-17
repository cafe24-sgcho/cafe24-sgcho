import subprocess
from datetime import datetime, timedelta

# 현재 시간
now = datetime.now()

# 9시간 전 시간
before = now - timedelta(hours=9)

# 시간 포맷 변경
before_str = before.strftime('%Y-%m-%dT%H:%M:%S.000')

# 커맨드에 적용
command = f"/home/apps/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group sgcho --topic cha_stream --reset-offsets --to-datetime {before_str} --execute"
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

command = "/home/apps/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cha_stream --consumer-property group.id=sgcho |grep stream_queue_key | grep mall_id\":\"syncombine1  |grep create_order |grep -v order_id\":\"20230810-0002702 |head -n 5"
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print(result.stdout.decode())




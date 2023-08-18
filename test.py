import subprocess
from datetime import datetime, timedelta

# 시간 입력 받기
time_str = input("시간을 입력하세요 (YYYY-MM-DD HH:MM:SS): ")

# 입력받은 시간을 datetime 객체로 변환
time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')

# 9시간 전 시간
before = time - timedelta(hours=9)

# 시간 포맷 변경
before_str = before.strftime('%Y-%m-%dT%H:%M:%S.000')

# 입력받은 시간과 9시간 전 시간 출력
print(f"입력받은 시간: {time_str}")
print(f"9시간 전 시간: {before.strftime('%Y-%m-%d %H:%M:%S')}")

# 커맨드에 적용
command = f"/home/apps/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group sgcho --topic cha_stream --reset-offsets --to-datetime {before_str} --execute"
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

command = "/home/apps/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic cha_stream --consumer-property group.id=sgcho |grep stream_queue_key | grep mall_id\":\"syncombine1  |grep create_order |grep -v order_id\":\"20230810-0002702 |head -n 5"
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print(result.stdout.decode())
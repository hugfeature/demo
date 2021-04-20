import json
import random
import datetime
import time

from dateutil.relativedelta import relativedelta
from kafka import KafkaProducer
from kafka.errors import KafkaError
#云侧
# producer = KafkaProducer(bootstrap_servers='192.168.175.234:9092,192.168.175.235:9092,192.168.175.236:9092')
# topic = 'whl_test'
#边缘侧
producer = KafkaProducer(
    bootstrap_servers='192.168.175.228:9092,192.168.175.228:9093,192.168.175.228:9094')
topic = 'wzx_test'


def test():
    try:
        n = 0
        while True:
            # msg_time = datetime.datetime.now() + relativedelta(years=1, months=1, days=0)
            msg_time = datetime.datetime.now()
            value = random.randint(0, 9999)
            label_list = ['260001010001000100010001010001', '260001010001000100010002010001',
                          '260001010001000100010003010001', '260001010001000100010006010001',
                          '260001010001000100010004010001', '260001010001000100010005010001',
                          '260001010001000100010007010001', '260001010001000100010008010001',
                          '260001010001000100010009010001', '260002010000000000000000040001',
                          '260001010000000000000000040001', '260001040019000100010001010004',
                          '260001040019000100010001010002', '260001010000000000000000020003',
                          '260001010000000000000000040005', '260001020002000100010001050009']
            label = random.choice(label_list)
            msg = {'Value': value, 'SysCode': label[0:8], 'ChannelCode': "001001",
                   'DeviceCode': label[8:24], 'DataID': label[24:30], 'UpdateCount': n, 'State': 1,
                   'Timestamp': int(msg_time.timestamp() * 1000)}
            n = n + 1
            print(n)
            send_msg = "[" + json.dumps(msg) + "]"
            producer.send(topic, send_msg.encode())
            if n == 400000:
                break
            # time.sleep(1)
    except KafkaError as e:
        print(e)
    finally:
        producer.close()
        print('done')


if __name__ == '__main__':
    time_start = datetime.datetime.now().timestamp()
    print(time_start)
    test()
    time_end = datetime.datetime.now().timestamp()
    print(time_end)
    print('耗时：' + str(time_end - time_start) + '秒')

from kinaggregator import deaggregator

import msgpack
import base64


class LogLessRecord:
    def __init__(self, **kwargs):
        self.message = kwargs["message"]
        self.timestamp = kwargs["timestamp"]
        self.level = kwargs["level"]
        self.source = kwargs["source"]
        self.fields = kwargs["fields"]


def logless_records(raw_kinesis_data):
    for data in deaggregator.iter_deaggregate_records(raw_kinesis_data):
        packed = base64.b64decode(data['kinesis']['data'])
        try:
            unpacked = msgpack.loads(packed, encoding='utf-8')
            record = LogLessRecord(**unpacked)
            yield record
        except Exception as e:
            print("Error while unpacking:", str(e))
        except KeyError as e:
            print("Error while creating record:", str(e))

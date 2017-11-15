# LogLess
> LogLess is a centralized logging/event stack using AWS Kinesis/Lambda. The AWS Lambda handler is used for processing incoming logs from Kinesis stream.

## Usage

Use the `logless_records` generator to process incoming records. The method returns a `LogLessRecord` object which can be used to process individual log entries.

Store the logs into ElasticSearch, use it to chech for alarm states etc. 


## Example

```python
import logless_lambda


def processor(event, context):
    for record in logless_lambda.logless_records(event['Records']):
        """
        Process records received from the logless_lambda library.
        """
        print("Received record", record.message, record.timestamp, record.level, record.source)

```

### License
Apache License 2.0
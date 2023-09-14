from google.api_core.exceptions import NotFound
from google.cloud.pubsub import PublisherClient

# TODO(developer): Replace these variables before running the sample.
project_id = "dp-website-397422"
topic_id = "send-email"

import send_email_pb2

publisher_client = PublisherClient()
topic_path = publisher_client.topic_path(project_id, topic_id)

try:
    # Get the topic encoding type.
    topic = publisher_client.get_topic(request={"topic": topic_path})
    
    with open('test_message.json', 'r') as file:
        data = file.read().replace('\n', '')
        print(f"Preparing a JSON-encoded message:\n{data}")

        future = publisher_client.publish(topic_path, data)
        print(f"Published message ID: {future.result()}")

except NotFound:
    print(f"{topic_id} not found.")
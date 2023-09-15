# gcp-email
Sends email through a google cloud function.

# GCP Create PubSub Schema
GCP Schema Docs: https://cloud.google.com/pubsub/docs/schemas#gcloud
gcloud pubsub schemas create send-email --type=protocol-buffer --definition-file=send_email.proto
# GCP Create PubSub Topic
gcloud pubsub topics create send-email --message-encoding=JSON --schema=send-email --schema-project=dp-website-397422 --project=dp-website-397422

# Examples
https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/functions/v2/pubsub

# function-framework cli
https://github.com/GoogleCloudPlatform/functions-framework-python/blob/main/src/functions_framework/_cli.py

# Testing
## First terminal
functions-framework --target=send_message --source=send_mail.py --port=5795 --debug 
## Second terminal
export PUBSUB_PROJECT_ID=my-project                                   ─╯
gcloud beta emulators pubsub start \
    --project=$PUBSUB_PROJECT_ID \
    --host-port=localhost:5795

# Compile the proto
https://protobuf.dev/getting-started/pythontutorial/

# Mailgun
https://github.com/mailgun/mailgun.js/blob/master/docs/modules.md

# Links
https://cloud.google.com/pubsub/docs/publisher
Installing Protoc (MacOS)
http://google.github.io/proto-lens/installing-protoc.html
Python Protocol Buffer Basics: https://protobuf.dev/getting-started/pythontutorial/
Receive Message from Proto Schema: https://cloud.google.com/pubsub/docs/samples/pubsub-subscribe-proto-messages

# Working Dir
Note: working directory in Cloud Run is /workspace

# OAuth
Using default service account on Cloud Run instance. I wansn't able to get this working but others have had success. See [this StackOverflow post](https://stackoverflow.com/questions/53202767/gae-attributeerror-credentials-object-has-no-attribute-with-subject/57092533#57092533). [And this one](https://stackoverflow.com/questions/64658391/how-can-i-grant-a-cloud-run-service-access-to-service-accounts-credentials-with).
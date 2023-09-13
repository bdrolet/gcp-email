deploy-schema:
	gcloud pubsub schemas commit send-email --type=protocol-buffer --definition-file=send_email.proto

deploy-function:
	gcloud functions deploy python-pubsub-function --gen2 --runtime=python311 --region=us-west1 --source=. --entry-point=send_message --trigger-topic=send-email
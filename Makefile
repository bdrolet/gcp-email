deploy-schema:
	gcloud pubsub schemas commit send-email --type=protocol-buffer --definition-file=send_email.proto

deploy-function:
	gcloud functions deploy send-email --gen2 --runtime=python311 --region=us-west1 --source=. --entry-point=send_message --trigger-topic=send-email

publish-message:
	gcloud pubsub topics publish send-email --message="{\"from_address\":\"ben@droletpsychiatry.com\",\"to_address\":[\"ben@drolet.cloud\"],\"subject\":\"Test Publish\",\"text\":\"Help I am stuck in the server\"}"

update-proto:
	protoc send_email.proto --python_out=. --pyi_out=.
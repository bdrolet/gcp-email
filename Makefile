deploy-schema:
	gcloud pubsub schemas commit send-email --type=protocol-buffer --definition-file=send_email.proto
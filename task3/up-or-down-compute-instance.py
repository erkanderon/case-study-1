from google.cloud import compute_v1
from collections import defaultdict
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--project", help='project id of the gcp', required=True)
parser.add_argument("--zone", help='zone of the machine', required=True)
parser.add_argument("--instance", help='machine instance id', required=True)
parser.add_argument("--operation", choices=["start", "stop"], help='whether you will stop or start?', required=True)
args = parser.parse_args()
print(args.echo)

# Using os we are storing the service account json key in the variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "key.json"

# Argument parse for given variables
project = args.project
zone = args.zone
instance = args.instance

instace_client = compute_v1.InstancesClient()


def start_instance():
	try:
		# Create a client
		client = compute_v1.InstancesClient()

		# Initialize request argument(s)
		request = compute_v1.StartInstanceRequest(
			instance=instance,
			project=project,
			zone=zone,
		)

		# Make the request
		response = client.start(request=request)

		print("VM Instance starting..")
		# Handle the response
		print(response.result())
		print('VM Instance started')
	except Exception as e:
		print("Exception occured: {}".format(e))


def stop_instance():
	try:
		# Create a client
		client = compute_v1.InstancesClient()

		# Initialize request argument(s)
		request = compute_v1.StopInstanceRequest(
			instance=instance,
			project=project,
			zone=zone,
		)

		# Make the request
		response = client.stop(request=request)

		print("VM Instance stopping..")
		# Handle the response
		response.result()
		print("VM Instance stopped")
	except Exception as e:
		print("Exception occured: {}".format(e))

def list_instances():

	request = compute_v1.AggregatedListInstancesRequest()
	request.project = project

	agg_list = instace_client.aggregated_list(request=request)

	all_instances = defaultdict(list)
	print("Instances found:")
	for zone, response in agg_list:
			if response.instances:
				all_instances[zone].extend(response.instances)
				print(f" {zone}:")
				for instance in response.instances:
					print(f" - {instance.name} ({instance.machine_type}) {instance.status}")

list_instances()

if args.operation == "start":
	start_instance()

if args.operation == "stop":
	stop_instance()

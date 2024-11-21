from chalice import Chalice
import boto3

app = Chalice(app_name='run-on-schedule')

instance_id = "id-1234123412341234123"
ec2 = boto3.client('ec2')

@app.schedule('cron(0 8 * * *)')
def daily_task():
    print("Running daily task at midnight") 
    response = ec2.start_instances(instance_id)

from pprint import pprint

import boto3
from botocore.exceptions import ClientError

client = boto3.client('resourcegroupstaggingapi', )
regions = boto3.session.Session().get_available_regions('ec2')

for region in regions:
    print(region)
    try:
        client = boto3.client('resourcegroupstaggingapi', region_name=region)
        pprint([x.get('ResourceARN') for x in client.get_resources().get('ResourceTagMappingList')])
    except ClientError as e:
        print(f'Could not connect to region with error: {e}')
    print()

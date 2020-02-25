import csv

from dagster import execute_pipeline, execute_solid, pipeline, solid


@solid
def hello_cereal(context):
    dataset_path = 'cereal.csv'
    with open(dataset_path, 'r') as f:
        cereals = [row for row in csv.DictReader(f)]

    message = f'Found {len(cereals)} cereals'
    context.log.info(message)

    return cereals


@pipeline
def hello_cereal_pipeline():
    hello_cereal()

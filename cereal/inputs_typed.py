import csv

from dagster import execute_pipeline, pipeline, solid


environment_dict = {
    'solids': {
        'read_csv': {'inputs': {'csv_path': {'value': 'cereal.csv'}}}
    }
}


@solid
def read_csv(context, csv_path: str):
    with open(csv_path, 'r') as fd:
        lines = [row for row in csv.DictReader(fd)]

    context.log.info('Read {n_lines} lines'.format(n_lines=len(lines)))
    return lines


@solid
def sort_by_calories(context, cereals):
    sorted_cereals = sorted(cereals, key=lambda cereal: int(cereal['calories']))
    context.log.info(
        'Least caloric cereal: {least_caloric}'.format(
            least_caloric=sorted_cereals[0]['name']
        )
    )
    context.log.info(
        'Most caloric cereal: {most_caloric}'.format(
            most_caloric=sorted_cereals[-1]['name']
        )
    )
    return {
        'least_caloric': sorted_cereals[0],
        'most_caloric': sorted_cereals[-1],
    }


@pipeline
def inputs_typed_pipeline():
    sort_by_calories(read_csv())

import os
import sys

import django
from dagster import execute_pipeline, pipeline, solid


# Add the project to sys.path, so that Python can find packages
PROJECT_ROOT = os.path.join(os.path.dirname(__file__), 'demo')
sys.path.append(PROJECT_ROOT)

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()


from customers.models import Customer


@solid
def hello_django_orm(context):
    number_of_customers = Customer.objects.count()
    message = f'Found {number_of_customers} customers!'
    context.log.info(message)
    return number_of_customers


@pipeline
def hello_django_orm_pipeline():
    hello_django_orm()


if __name__ == '__main__':
    result = execute_pipeline(hello_django_orm_pipeline)
    assert result.success

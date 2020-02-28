from dagster import RepositoryDefinition

from complex_pipeline import complex_pipeline
from hello_cereal import hello_cereal_pipeline


def define_repo():
    return RepositoryDefinition(
        name='hello_cereal_repository',
        pipeline_dict={
            'hello_cereal_pipeline': lambda: hello_cereal_pipeline,
            'complex_pipeline': lambda: complex_pipeline,
        },
    )

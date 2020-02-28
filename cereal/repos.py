from dagster import RepositoryDefinition

from complex_pipeline import complex_pipeline
from hello_cereal import hello_cereal_pipeline
from inputs import inputs_pipeline
from serial_pipeline import serial_pipeline


def define_repo():
    return RepositoryDefinition(
        name='hello_cereal_repository',
        pipeline_dict={
            'complex_pipeline': lambda: complex_pipeline,
            'hello_cereal_pipeline': lambda: hello_cereal_pipeline,
            # 'inputs_pipeline': lambda: inputs_pipeline,
            # 'serial_pipeline': lambda: serial_pipeline,
        },
    )

from contextlib import ExitStack
from unittest.mock import patch

from dagster import execute_pipeline, execute_solid

from hello_django_orm import hello_django_orm, hello_django_orm_pipeline


def test_hello_django_orm_solid():
    with ExitStack() as stack:
        mock_customer = stack.enter_context(
            patch('hello_django_orm.Customer.objects.count', return_value=5)
        )
        res = execute_solid(hello_django_orm)

    assert res.success
    assert res.output_value() == 5


def test_hello_django_orm_pipeline():
    res = execute_pipeline(hello_django_orm_pipeline)
    assert res.success
    assert len(res.solid_result_list) == 1
    for solid_res in res.solid_result_list:
        assert solid_res.success

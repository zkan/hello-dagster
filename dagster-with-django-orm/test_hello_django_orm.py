from dagster import execute_pipeline

from hello_django_orm import hello_django_orm_pipeline


def test_hello_django_orm_pipeline():
    res = execute_pipeline(hello_django_orm_pipeline)
    assert res.success

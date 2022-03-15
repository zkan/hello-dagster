from dagster import build_op_context, ExecuteInProcessResult

from hello_world import get_name, hey, hey_job


def test_get_name():
    assert get_name() == "Kan"


def test_hey():
    context = build_op_context()
    assert hey(context, "Yo") is None


def test_hey_job():
    result = hey_job.execute_in_process()

    assert isinstance(result, ExecuteInProcessResult)
    assert result.success
    assert result.output_for_node("get_name") == "Kan"
    assert result.output_for_node("hey") is None

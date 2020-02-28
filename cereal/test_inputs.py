from dagster import execute_solid

from inputs import sort_by_calories


def test_sort_by_calories():
    res = execute_solid(
        sort_by_calories,
        input_values={
            'cereals': [
                {'name': 'just_lard', 'calories': '1100'},
                {'name': 'dry_crust', 'calories': '20'},
                {'name': 'burger', 'calories': '550'},
            ]
        },
    )
    assert res.success
    output_value = res.output_value()
    assert output_value['most_caloric']['name'] == 'just_lard'
    assert output_value['least_caloric']['name'] == 'dry_crust'

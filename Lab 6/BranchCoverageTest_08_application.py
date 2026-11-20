
from ski_resort_pass import (
    process_resort_bookings,
    check_chairlift_anemometer,
)


def test_all_pass_durations():
    groups = [
        {"is_active": True, "duration": "season",
         "skiers": [{"age": 30}]},
        {"is_active": True, "duration": "full_day",
         "skiers": [{"age": 30}]},
        {"is_active": True, "duration": "half_day",
         "skiers": [{"age": 30}]},
    ]
    result = process_resort_bookings(groups, 0)
    assert result["total_revenue"] == 430.0


def test_inactive_group():
    groups = [
        {"is_active": False},
        {"is_active": True, "duration": "full_day",
         "skiers": [{"age": 30}]},
    ]
    result = process_resort_bookings(groups, 0)
    assert result["total_revenue"] == 80.0


def test_invalid_duration():
    groups = [{
        "is_active": True,
        "duration": "weekly",
        "skiers": [{"age": 30}],
    }]
    assert process_resort_bookings(groups, 0)["status"] == "ZERO_SALES"


def test_child_adult_senior_boundaries():
    groups = [{
        "is_active": True,
        "duration": "full_day",
        "skiers": [
            {"age": 11},
            {"age": 12},
            {"age": 64},
            {"age": 65},
        ],
    }]
    result = process_resort_bookings(groups, 0)
    assert result["total_revenue"] == 264.0


def test_invalid_ages():
    groups = [{
        "is_active": True,
        "duration": "full_day",
        "skiers": [{"age": 0}, {"age": -1}],
    }]
    assert process_resort_bookings(groups, 0)["status"] == "ZERO_SALES"


def test_gear_rental_true_and_false():
    groups = [{
        "is_active": True,
        "duration": "full_day",
        "skiers": [
            {"age": 30, "gear_rental": True},
            {"age": 30, "gear_rental": False},
        ],
    }]
    result = process_resort_bookings(groups, 0)
    assert result["total_revenue"] == 195.0


def test_blackout_full_day():
    groups = [{
        "is_active": True,
        "duration": "full_day",
        "skiers": [{"age": 30, "blackout_override": True}],
    }]
    assert process_resort_bookings(
        groups, 0
    )["total_revenue"] == 40.0


def test_blackout_half_day():
    groups = [{
        "is_active": True,
        "duration": "half_day",
        "skiers": [
            {"age": 30, "blackout_override": True},
            {"age": 30},
        ],
    }]
    assert process_resort_bookings(
        groups, 0
    )["total_revenue"] == 0.0


def test_blackout_season():
    groups = [{
        "is_active": True,
        "duration": "season",
        "skiers": [{"age": 30, "blackout_override": True}],
    }]
    assert process_resort_bookings(
        groups, 0
    )["total_revenue"] == 150.0


def test_locker_true_and_false():
    groups = [
        {
            "is_active": True,
            "duration": "full_day",
            "skiers": [{"age": 30}],
            "includes_lodge_locker": True,
        },
        {
            "is_active": True,
            "duration": "full_day",
            "skiers": [{"age": 30}],
            "includes_lodge_locker": False,
        },
    ]
    assert process_resort_bookings(
        groups, 10
    )["total_revenue"] == 170.0


def test_audit_review():
    groups = [{
        "is_active": True,
        "duration": "full_day",
        "skiers": [{"age": 0} for _ in range(5)],
    }]
    assert process_resort_bookings(
        groups, 0
    )["status"] == "AUDIT_REVIEW"


def test_exactly_four_rejections():
    groups = [{
        "is_active": True,
        "duration": "full_day",
        "skiers": [{"age": 0} for _ in range(4)],
    }]
    assert process_resort_bookings(
        groups, 0
    )["status"] == "ZERO_SALES"


def test_zero_sales():
    assert process_resort_bookings([], 0)["status"] == "ZERO_SALES"


def test_completed():
    groups = [{
        "is_active": True,
        "duration": "full_day",
        "skiers": [{"age": 30}],
    }]
    assert process_resort_bookings(
        groups, 0
    )["status"] == "COMPLETED"


def test_invalid_inputs():
    import pytest

    with pytest.raises(ValueError):
        process_resort_bookings("invalid", 0)

    with pytest.raises(ValueError):
        process_resort_bookings([], -1)


def test_no_wind_data():
    assert check_chairlift_anemometer([]) == "NO_DATA"


def test_empty_lift_readings():
    assert check_chairlift_anemometer([[]]) == "SAFE_OPERATION"


def test_safe_wind():
    assert check_chairlift_anemometer(
        [[20, 30, 45]]
    ) == "SAFE_OPERATION"


def test_one_high_wind_reading():
    assert check_chairlift_anemometer(
        [[46]]
    ) == "SAFE_OPERATION"


def test_high_wind_reset():
    assert check_chairlift_anemometer(
        [[46, 40, 47]]
    ) == "SAFE_OPERATION"


def test_consecutive_high_winds():
    assert check_chairlift_anemometer(
        [[46, 47]]
    ) == "SUSPEND_LIFT"


def test_three_consecutive_high_winds():
    assert check_chairlift_anemometer(
        [[46, 47, 48]]
    ) == "SUSPEND_LIFT"


def test_high_winds_on_separate_lifts():
    assert check_chairlift_anemometer(
        [[46], [47]]
    ) == "SAFE_OPERATION"

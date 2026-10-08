import pytest

from miniforecast.baseline import predict_mean


def test_predict_mean_repeats_the_mean():
    assert predict_mean([1,2,3],2)==[2.0,2.0]


def test_predict_mean_output_length_matches_horizon():
    assert len(predict_mean([1, 2, 3], 5)) == 5


def test_predict_mean_rejects_empty_history():
    with pytest.raises(ValueError):
        predict_mean([], 3)

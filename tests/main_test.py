from taxi_processing_pkg.main import get_taxis, get_spark


def test_get_taxis_count():
    taxis = get_taxis(get_spark())
    assert taxis.count() > 5


def test_get_taxis_schema():
    taxis = get_taxis(get_spark())
    assert "tpep_pickup_datetime" in taxis.columns
    assert "tpep_dropoff_datetime" in taxis.columns
    assert "trip_distance" in taxis.columns
    assert "fare_amount" in taxis.columns
    assert "pickup_zip" in taxis.columns
    assert "dropoff_zip" in taxis.columns
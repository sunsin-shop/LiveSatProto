from livesatproto.where_now import get_currentLocation
from datetime import datetime

def test_get_currentLocation():
     # 함수 호출
    result = get_currentLocation("2025-01-24T00:00:00Z", 45.0, 37.7749, -122.4194)

    # 리턴 값이 존재하는지 검증
    assert result is not None
    assert "satellite_position" in result
    assert "latitude" in result["satellite_position"]
    assert "longitude" in result["satellite_position"]
    assert "altitude" in result["satellite_position"]
    assert "satellite_id" in result
    assert "timestamp" in result

    # 추가적으로 timestamp가 올바른 포맷인지 검증 (ISO 8601 형식)
    timestamp = result["timestamp"]
    assert datetime.fromisoformat(timestamp[:-1])

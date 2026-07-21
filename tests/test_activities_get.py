def test_get_activities_returns_data_and_cache_headers(client):
    # Arrange

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert "Chess Club" in payload
    assert response.headers["cache-control"] == "no-store, no-cache, must-revalidate, max-age=0"

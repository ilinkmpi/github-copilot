"""
test_app.py

Unit tests for the Mergington High School Management System API (src/app.py).
"""

from fastapi.testclient import TestClient
from src.app import app
import pytest

client = TestClient(app)

# Test root redirect

def test_root_redirect():
    response = client.get("/")
    assert response.status_code == 200 or response.status_code == 307
    assert "text/html" in response.headers["content-type"]

# Test get activities

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "participants" in data["Chess Club"]

# Test signup for activity

def test_signup_for_activity():
    email = "testuser@mergington.edu"
    activity = "Chess Club"
    # Remove if already present
    client.post(f"/activities/{activity}/unregister?email={email}")
    response = client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 200
    assert f"Signed up {email} for {activity}" in response.json()["message"]
    # Duplicate signup should fail
    response2 = client.post(f"/activities/{activity}/signup?email={email}")
    assert response2.status_code == 400
    assert "Already signed up" in response2.json()["detail"]

# Test unregister from activity

def test_unregister_from_activity():
    email = "testuser2@mergington.edu"
    activity = "Programming Class"
    # Ensure user is signed up
    client.post(f"/activities/{activity}/signup?email={email}")
    response = client.post(f"/activities/{activity}/unregister?email={email}")
    assert response.status_code == 200
    assert f"Unregistered {email} from {activity}" in response.json()["message"]
    # Unregister again should fail
    response2 = client.post(f"/activities/{activity}/unregister?email={email}")
    assert response2.status_code == 400
    assert "not registered" in response2.json()["detail"]

# Test invalid activity

def test_invalid_activity():
    response = client.post("/activities/Nonexistent/signup?email=foo@bar.com")
    assert response.status_code == 404
    response2 = client.post("/activities/Nonexistent/unregister?email=foo@bar.com")
    assert response2.status_code == 404

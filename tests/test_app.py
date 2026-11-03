import unittest
from app import app


class FlaskApplicationTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Docker Containerization Complete!",
            response.data
        )

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {
                "status": "healthy",
                "service": "flask-docker-app"
            }
        )

    def test_unknown_route(self):
        response = self.client.get("/unknown")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()

from django.test import TestCase
from rest_framework.test import APIClient
from .models import Worker, Status, Order


class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.worker = Worker.objects.create(name="Worker 1")
        self.status = Status.objects.create(name="Pending")
        self.order = Order.objects.create(description="Order 1", worker=self.worker, status=self.status)

    def test_get_orders(self):
        response = self.client.get('/orders/')
        self.assertEqual(response.status_code, 200)

    def test_create_order(self):
        data = {
            "description": "Order 2",
            "worker": self.worker.id,
            "status": self.status.id
        }
        response = self.client.post('/orders/', data, format='json')
        self.assertEqual(response.status_code, 201)

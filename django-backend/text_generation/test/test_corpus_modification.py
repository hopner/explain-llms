from django.test import TestCase
from rest_framework.test import APIClient
from users.models import User
import uuid

class CorpusModificationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.guid = str(uuid.uuid4())
        res = self.client.post('/api/users/', {'guid': self.guid}, format='json')
        self.assertEqual(res.status_code, 200, f"User creation failed: {res.data}")
        self.client.cookies['user_guid'] = self.guid

    def test_user_creation(self):
        user = User.objects.get(guid=self.guid)
        self.assertIsNotNone(user)

    def test_read_book_updates_corpus(self):
        res = self.client.post('/api/add-feature/', {'feature_id': 'read_book'}, format='json')
        self.assertEqual(res.status_code, 200, res.data)
        user = User.objects.get(guid=self.guid)
        selected = user.model_config.get("selected_features", [])
        self.assertIn('read_book', selected)
        ids = [entry.get("id") for entry in user.model_config.get("knowledge", []) if entry.get("id")]
        self.assertIn('moby_dick', ids)

    def test_read_another_updates_corpus(self):
        self.client.post('/api/add-feature/', {'feature_id': 'read_book'}, format='json')
        res = self.client.post('/api/add-feature/', {'feature_id': 'read_another'}, format='json')
        self.assertEqual(res.status_code, 200, res.data)
        user = User.objects.get(guid=self.guid)
        selected = user.model_config.get("selected_features", [])
        self.assertIn('read_another', selected)
        ids = [entry.get("id") for entry in user.model_config.get("knowledge", []) if entry.get("id")]
        self.assertIn('moby_dick', ids)
        self.assertIn('alice', ids)

    def test_set_corpus_overwrites_ids(self):
        self.client.post('/api/add-feature/', {'feature_id': 'read_book'}, format='json')
        self.client.post('/api/add-feature/', {'feature_id': 'read_another'}, format='json')

        res = self.client.post('/api/set-corpus/', {'ids': ['les_miserables', 'monte_cristo']}, format='json')
        self.assertEqual(res.status_code, 200, res.data)

        user = User.objects.get(guid=self.guid)
        new_ids = [e.get('id') for e in user.model_config.get('knowledge', [])]
        self.assertEqual(sorted(new_ids), sorted(['les_miserables', 'monte_cristo']))

    def test_set_corpus_overwrites_vocab(self):
        self.client.post('/api/add-feature/', {'feature_id': 'read_book'}, format='json')
        self.client.post('/api/add-feature/', {'feature_id': 'read_another'}, format='json')

        res = self.client.post('/api/set-corpus/', {'ids': ['les_miserables']}, format='json')
        self.assertEqual(res.status_code, 200, res.data)

        model = res.data.get('model', {})
        vocab = model.get('vocab', [])
        self.assertIn('Valjean', vocab)


    def test_predict_endpoint_returns_text(self):
        self.client.post('/api/add-feature/', {'feature_id': 'read_book'}, format='json')
        self.client.post('/api/set-corpus/', {'ids': ['les_miserables']}, format='json')

        res = self.client.post('/api/predict/', {'prompt': 'Once upon a time'}, format='json')
        self.assertEqual(res.status_code, 200, res.data)
        self.assertIn('prediction', res.data)
        self.assertIsInstance(res.data['prediction'], str)
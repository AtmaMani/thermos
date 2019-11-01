import unittest
import requests
import json

class TestThermos(unittest.TestCase):
    base_address = 'http://localhost:5000'

    def test_root(self):
        resp = requests.get(self.base_address + '/')
        self.assertEqual(resp.status_code, 200)

    def test_hello_no_args(self):
        no_args = requests.get(self.base_address + '/hello')
        self.assertEqual(no_args.text, 'Hello ')

    def test_hello_named_args(self):
        params = {'name':'tester'}
        named_args = requests.get(self.base_address + '/hello', params)
        self.assertEqual(named_args.text, 'Hello tester')

    def test_genUniqueRandom(self):
        params = {'numRandom': 20, 'upperLimit': 30}
        resp = requests.get(self.base_address + '/genUniqueRandom', params)
        resp_json = json.loads(resp.text)

        self.assertEqual(len(resp_json), params['numRandom'])

if __name__ == '__main__':
    unittest.main()

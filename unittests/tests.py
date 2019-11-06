import unittest
import requests
import json


class TestThermos(unittest.TestCase):
    base_address = 'http://localhost:5000' # for local dev
    # base_address = 'http://atma-thermos.herokuapp.com' # for testing production

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

    def test_eyeFromAbove_get(self):
        resp = requests.get(self.base_address + '/eyeFromAbove')
        self.assertEqual(resp.status_code, 200)

    def test_eyeFromAbove_post(self):
        params = {'address':'2094 W Redlands Blvd, Redlands, CA',
                  'date':'2014-5-6'}
        resp = requests.post(self.base_address + '/eyeFromAbove', data=params)

        self.assertEqual(resp.status_code, 200)

    def test_addresses_post(self):
        slug = '/addresses'
        address_list = ['505 New Jersey St, Redlands, CA',
                     '27481 San Bernardino Ave, Redlands, CA',
                     '1919 Atlas Dr, Riverside, CA']
        address_str = ';'.join(address_list)
        params = {'addressList':address_str}

        resp = requests.post(self.base_address + slug, data=params)
        self.assertEqual(200, resp.status_code)

    def test_addresses_get(self):
        slug = '/addresses'
        resp = requests.get(self.base_address + slug)
        resp_json = json.loads(resp.text)
        self.assertIsInstance(resp_json, list)
        self.assertGreaterEqual(len(resp_json), 1)
        print(resp_json)

    def test_addresses_id_get(self):
        slug = '/addresses/2'
        resp = requests.get(self.base_address + slug)
        resp_json = json.loads(resp.text)
        self.assertTrue('search_time' in resp_json)
        print(resp_json)

    def test_addresses_id_put_get(self):
        slug = '/addresses/2'
        params = {'address':'changed via test'}
        resp = requests.put(self.base_address + slug, params)

        # verify it was changed
        resp = requests.get(self.base_address + slug)
        resp_json = json.loads(resp.text)
        self.assertTrue('search_time' in resp_json)
        self.assertEqual(resp_json['search_string'], 'changed via test')
        print(resp_json)


if __name__ == '__main__':
    unittest.main()

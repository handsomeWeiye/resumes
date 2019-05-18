import unittest

from flask import abort

from myresume import app,db


class ResumeTestCase(unittest.TestCase):

    def setUp(self):
        app.config.update(
            TESTING=True,
            WTF_CRSF_ENABLE=False,
            SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
        )
        db.create_all()
        self.client = app.test_client()
        self.runner = app.test_cli_runner()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_app_exist(self):
        self.assertFalse(app is None)

    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])


    def test_500_page(self):
        # create route to abort the request with the 500 Error
        @app.route('/500')
        def internal_server_error_for_test():
            abort(500)

        response = self.client.get('/500')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 500)




    def test_index_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertIn('Resume',data)



    def test_404_page(self):
        response = self.client.get('/nothing')
        data = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
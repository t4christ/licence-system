from unittest import TestCase
from licence import Customer,Plan,Website



class CustomerTestCase(TestCase):
    customer = Customer()
    plan = Plan()
    website = Website()
    customer_object = {'name': 'jean baptiste', 'email': 'faith@gmail.com', 
                        'password': 'password'}
    
    def test_create_customer(self):
        new_customer = self.customer.create_customer('jean baptiste','faith@gmail.com',
                                                    'password')
        self.assertEqual(new_customer,self.customer_object)

    
    def test_customer_is_customer_instance(self):
        self.assertIsInstance(self.customer,Customer)

    def test_customer_keyerror_if_exist(self):
            with self.assertRaises(KeyError):
                self.customer.create_customer('jean baptiste','faith@gmail.com','password')


    def test_get_customer(self):
            new_customer = self.customer.get_customer('jean baptiste')
            self.assertEquals(new_customer,self.customer_object)
    


class PlanTestCase(TestCase):
    plan = Plan()
    
    plan_object_single = {'customer_name': 'jean baptiste', 'plan': 'Single', 'price': 49,
                          'no_websites':1}
    plan_object_plus = {'customer_name': 'jean baptiste', 'plan': 'Plus', 'price': 99,
                        'no_websites':3}
    plan_object_unlimited = {'customer_name': 'jean baptiste', 'plan': 'Unlimited', 
                            'price': 249,'no_websites':50}
    
    def test_create_single_plan(self):
        new_plan = self.plan.create_plan('jean baptiste','Single')
        self.assertEqual(new_plan,self.plan_object_single)
    
    def test_create_plus_plan(self):
        new_plan = self.plan.create_plan('jean baptiste','Plus')
        self.assertEqual(new_plan,self.plan_object_plus)

    def test_create_unlimited_plan(self):
        new_plan = self.plan.create_plan('jean baptiste','Unlimited')
        self.assertEqual(new_plan,self.plan_object_unlimited)

    
    def test_plan_is_plan_instance(self):
        self.assertIsInstance(self.plan,Plan)

    def test_get_plan(self):
        self.assertEqual(self.plan.get_plan('jean baptiste'),self.plan_object_unlimited)


    def test_update_plan(self):
            get_plan = self.plan.update_plan('jean baptiste','Plus')
            self.assertEquals(get_plan,self.plan_object_plus)


class WebsiteTestCase(TestCase):
    website = Website()
    website_object = {'customer_name': 'jean baptiste', 'url': 'https://www.web.com'}
    
    def test_create_website(self):
        new_website = self.website.create_url('jean baptiste')
        self.assertEqual(new_website,self.website_object)

    
    def test_website_is_customer_instance(self):
        self.assertIsInstance(self.website,Website)

    def test_website_keyerror_if_exist(self):
            with self.assertRaises(KeyError):
                self.website.create_url('jean baptiste')


    def test_get_website(self):
            new_website = self.website.get_website('jean baptiste')
            self.assertEquals(new_website,self.website_object)
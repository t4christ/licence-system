from datetime import date
from dateutil.relativedelta import relativedelta

# Customers dummy record accessible by plan and website object 
# before creating a plan and website since a plan and a website 
# can only be created by a registered customer
customers = {}

class Customer():
    def __init__(self):
        self.name = 'name'
        self.email = 'email@email.com'
        self.password = 'password'


    def get_customer(self,name):
        return customers.get(name,f'Sorry {name} does not exist')

    @property
    def get_all_customer(self):
        return customers

    def create_customer(self,name,email,password):
        if len(customers) > 0:
            #Check if a customer already exist
            for customer_key,customer_val in customers.items():
                if customer_key == name:
                    raise KeyError(f'{name} already exists')
                elif customer_val['email'] == email:
                    raise KeyError(f'{email} already exists')
        #If not go ahead and create a customer
        customers[name] = {'name':name,'email':email,'password':password}
        return customers.get(name)



    def __str__(self):
        return f'Your name is {self.name} and your email address is \
                {self.email}'


###################### Plan Class #########################
class Plan():
    customer_plans = {}
    subscription = date.today()
    sub_renewal_date = subscription + relativedelta(years=1)
    plans = {'Single':'Single','Plus':'Plus','Unlimited':'Unlimited'}
    price_plans = {'Single':49,'Plus':99,'Unlimited':249}
    no_of_website_plan = {'Single':1,'Plus':3}

    def __init__(self):
        self.name = 'Single'
        self.price = 49
        self.no_of_websites = 1


    def get_plan(self,customer_name):
            return self.customer_plans.get(customer_name,f'Sorry {customer_name} with \
                                                    plan does not exist')

    def create_plan(self,customer_name,plan):
        #Check if a customer_name already exist
        if customer_name in customers:
            if len(self.plans) > 0:
                #Check if a customer plan already exist
                for plan_key,plan_val in self.plans.items():
                    if plan_key == customer_name:
                        raise KeyError(f'{customer_name} with plan already exists')

            # If customer with a plan does not exist go ahead and create a plan
            if self.plans[plan]:
                if self.plans[plan] == 'Unlimited':
                    no_of_websites = int(input('Enter number of websites for your unlimited\
                                         plan => '))
                    self.customer_plans[customer_name] = {'customer_name':customer_name,\
                                            'plan':plan,'price':self.price_plans.get(plan),\
                                             'no_websites':no_of_websites}
                    customers.get(customer_name).update({'subscribed':self.subscription,\
                                            'subscription_renewal':self.sub_renewal_date})
                else:
                    self.customer_plans[customer_name] = {'customer_name':customer_name,
                                                'plan':plan,'price':self.price_plans.get(plan),\
                                                'no_websites':self.no_of_website_plan.get(plan)}
                    customers.get(customer_name).update({'subscribed':self.subscription,\
                                                'subscription_renewal':self.sub_renewal_date})

            return self.customer_plans.get(customer_name)
        else:
            raise NotImplementedError('You must be a customer to create a plan')


    
    def update_plan(self,customer_name,plan):
        #Check if a customer_name exist
        if customer_name in self.customer_plans and plan in self.plans:
            #If it exists go ahead an update the plan
            if self.plans[plan] == 'Unlimited':
                no_of_websites = input('Enter number of websites for your unlimited plan => ')
                self.customer_plans.update({customer_name:{'customer_name':customer_name,\
                                            'plan':plan,'price':self.price_plans.get(plan),\
                                             'no_websites':no_of_websites}})
            else:
                self.customer_plans.update({customer_name:{'customer_name':customer_name,\
                                            'plan':plan,'price':self.price_plans.get(plan),\
                                            'no_websites':self.no_of_website_plan.get(plan)}})          
        else:
            raise KeyError('Customer name with a plan does not exist')
        return self.customer_plans.get(customer_name)
        
    def remove_plan(self,plan_for_customer_name):
        #Check if a customer plan exist
        if self.customer_plans.get(plan_for_customer_name):
            #If it exist prompt for a comfirmation before deleting
            answer = input('Are you sure you want to delete plan (yes/no) => ')
            if answer == 'yes':
                del self.customer_plans[plan_for_customer_name]
                return f'Your plan has been successfully  deleted'
            else:
                print(f'Delete action cancelled')
                return self.customer_plans.get(plan_for_customer_name)
        else:
            return 'Customer name does not exist or has been deleted'

    def __str__(self):

        return f'Your plan is detail is {self.name} for {self.price} and \
                {self.no_of_websites} website(s)'

    
###################### Website Class #########################
class Website():
    customer_websites ={}
    def __init__(self):
        self.url = 'https://www.customerwebsite.com'

    def create_url(self,customer_name):
        #Check if a customer_name exist
        if customer_name in customers:
            if len(self.customer_websites) > 0:
                #If customer_name exist check if the customer already has a website
                for website_key,website_val in self.customer_websites.items():
                    if website_key == customer_name:
                        raise KeyError(f'{customer_name} with website already exists')

            #If a website for that customer does not exist go ahead and create one
            website_url = input('Enter a website url for your website \
                                (e.g www.mywebsite.com) => ')
                
            self.customer_websites[customer_name] = {'customer_name':customer_name,\
                                                    'url':f'https://{website_url}'}
            return self.customer_websites.get(customer_name)

        else:
            raise NotImplementedError('You must be a customer to create a website url')

    def get_website(self,customer_name):
            return self.customer_websites.get(customer_name,f'Sorry {customer_name} with\
                                               website does not exist')

    def __str__(self):
            return f'Your website url is {self.url}'




######################## Test Data for Customer ##########################
# c = Customer()
# c.create_customer('jean baptiste','jean@gmail.com','password')
# c.create_customer('marchand arvier','marchand@gmail.com','password')
# print(c.get_all_customer)

######################## Test Data for Plan ##########################                
# p = Plan()
# print(p.create_plan('jean baptiste','Single'))
# print(c.get_all_customer)
# print(p.customer_plans)
# print(p.update_plan('jean baptiste','Unlimited'))
# print(p.remove_plan('jean baptiste'))
# print(p.customer_plans)


######################## Test Data for Website ##########################
# w = Website()
# print(w.create_url('jean baptiste'))
# print(w)
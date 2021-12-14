from django.test import TestCase , Client
from .models import Task
from django.db.models import Max

class TasksTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Initializing test object
        test_task1=Task.objects.create(
            id="1" , state= "DRFT", title="Ideas"
        )
        test_task1.save()

        test_task2=Task.objects.create(
            id="2" , state= "ACTV", title="Implementation"
        )
        test_task2.save()

        test_task3=Task.objects.create(
            id="3" , state= "DN", title="Testing"
        )
        test_task3.save()

        test_task4=Task.objects.create(
            id="4" , state= "ARCH", title="Publication"
        )
        test_task4.save()

    # Testing the content inside each instance in the database
    def test_task_content(self):

        task1 = Task.objects.get(id=1)
        id1= f'{task1.id}'
        state1 = f'{task1.state}'
        title1 = f'{task1.title}'

        task2 = Task.objects.get(id=2)
        id2= f'{task2.id}'
        state2 = f'{task2.state}'
        title2 = f'{task2.title}'


        task3 = Task.objects.get(id=3)
        id3= f'{task3.id}'
        state3 = f'{task3.state}'
        title3 = f'{task3.title}'

        task4 = Task.objects.get(id=4)
        id4= f'{task4.id}'
        state4 = f'{task4.state}'
        title4 = f'{task4.title}'



        # Comparing initialized test object to raw data

        # Test 1
        self.assertEqual(id1 , "1")
        self.assertEqual(state1 , "DRFT")
        self.assertEqual(title1 , "Ideas")

        # Test 2
        self.assertEqual(id2 , "2")
        self.assertEqual(state2 , "ACTV")
        self.assertEqual(title2 , "Implementation")

        # Test 3
        self.assertEqual(id3 , "3")
        self.assertEqual(state3 , "DN")
        self.assertEqual(title3 , "Testing")

        # Test 4
        self.assertEqual(id4 , "4")
        self.assertEqual(state4 , "ARCH")
        self.assertEqual(title4 , "Publication")

    # Test for validity of next state function on the state field
    def test_task_state(self):
        task = Task.objects.get(id=1)
        state = f'{task.state}'
        task.nextState()
        nextState = f'{task.state}'
        if state == "DRFT":
            self.assertEqual(nextState , "ACTV")
        elif state == "ACTV":
            self.assertEqual(nextState , "DN")
        elif state == "DN":
            self.assertEqual(nextState , "ARCH")
        elif state == "ARCH":
            self.assertEqual(nextState , "ARCH")
    
    # Test for validity/invalidity of next state function on the status codes response
    def test_valid_next_state(self):
        task1 = Task.objects.get(id=1)
        task2 = Task.objects.get(id=2)
        task3 = Task.objects.get(id=3)
        task4 = Task.objects.get(id=4)

        c = Client()
        
        response1 = c.get(f"/api/v1/{task1.id}/advance")
        response2 = c.get(f"/api/v1/{task2.id}/advance")
        response3 = c.get(f"/api/v1/{task3.id}/advance")
        response4 = c.get(f"/api/v1/{task4.id}/advance")
        self.assertEqual(response1.status_code , 200)
        self.assertEqual(response2.status_code , 200)
        self.assertEqual(response3.status_code , 200)
        self.assertEqual(response4.status_code , 400)
    

    # Test for validity/invalidity of archiving an non/already archived state function on the status codes response
    def test_archived_next_state(self):
        task1 = Task.objects.get(id=1)
        task4 = Task.objects.get(id=4)

        c=Client()

        response1 = c.get(f"/api/v1/{task1.id}/archive")
        response4 = c.get(f"/api/v1/{task4.id}/archive")
        self.assertEqual(response1.status_code , 200)
        self.assertEqual(response4.status_code , 400)

    # Test for GET list of all tasks
    def test_task_list(self):
        c = Client()

        response = c.get("/api/v1/")
        self.assertEqual(response.status_code , 200)

    # Test for GET a single task
    def test_valid_task_details(self):
        task = Task.objects.get(id=1)

        c= Client()

        response = c.get(f"/api/v1/{task.id}/")
        self.assertEqual(response.status_code , 200)

    # Test for GET an invalid task id
    def test_invalid_task_details(self):
        max_id = Task.objects.all().aggregate(Max("id"))["id__max"]

        c= Client()

        response = c.get(f"/api/v1/{max_id+1}/")
        self.assertEqual(response.status_code , 404)

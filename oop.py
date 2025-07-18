class emplyee:

    def __init__(self):

        print("all the atributes and methods")
        self.id=123
        self.salary=50000
        self.designation="SDE"
        print('all the atributes and method are initialized')
    
    def travel(self, destination):
        print(f"employee is now travelling to {destination}")

    def presentation(self, topic):
        print(f"employee is presenting the {topic}")
# create an object/instance of class
sam=emplyee()
sam.presentation(topic='artifical intelligence')
sam.travel(destination='lahore')
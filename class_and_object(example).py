# class ModelTrainer:
#     def __init__(self,model,data):
#         self.model=model
#         self.data=data
    
#     def train(self):
#         print(f"training {self.model} on {self.data}")

# #object
# trainer=ModelTrainer(model='RandomForest',data='titanic.csv')
# trainer.train()
        
class ModelDeployer:
    def __init__(self, model, environment):
        self.model=model
        self.environment=environment

        def deploy(self):
            print(f"Deploying {self.model} to {self.environment}")
    
    # object 
    deployer = ModelDeployer(model='SVM', environment='AWS')
    deployer.deploy()

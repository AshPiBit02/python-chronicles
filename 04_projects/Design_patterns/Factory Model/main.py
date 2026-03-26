from app import ModelFactory,ClassificationModelFactory,RegressionModelFactory
def clientt_code(factory:ModelFactory,data,labels):
    model=factory.create_model()
    evaluator=factory.create_evaluator()
    visualizer=factory.create_visualizer()

    predictions=model.train(data)
    results=evaluator.evaluate(predictions,labels)
    visualizer.visualize(results)
Factory_map={"classification":lambda: ClassificationModelFactory(),
             "regression":lambda: RegressionModelFactory()
             }
def get_factory(task_type:str) -> ModelFactory:
    try:
        return Factory_map[task_type]() # class lambda to instantiate
    except KeyError:
        raise ValueError(f"Unknown ModelFactory: {task_type}")
    
    
print(f"{'-'*7} Regression Model Factory {'-'*7}")
factory=get_factory("classification")
clientt_code(factory,[1.5,5.2,6.7,8.0],"NVME")


print(f"{'-'*7} Regression Model Factory {'-'*7}")
factory=get_factory("regression")
clientt_code(factory,[1.5,5.2,6.7,8.0],"NVME")
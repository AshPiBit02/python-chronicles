from app import ModelFactory,ClassificationModelFactory,RegressionModelFactory
def clientt_code(factory:ModelFactory,data,labels):
    model=factory.create_model()
    evaluator=factory.create_evaluator()
    visualizer=factory.create_visualizer()

    predictions=model.train(data)
    results=evaluator.evaluate(predictions,labels)
    visualizer.visualize(results)
clientt_code(RegressionModelFactory(),[1.5,5.2,6.7,8.0],"NVME")
clientt_code(ClassificationModelFactory(),[1.5,5.2,6.7,8.0],"NVME")
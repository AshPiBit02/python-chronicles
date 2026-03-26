# Abstract Products
class Model:
    def train(self,data):
        raise NotImplementedError
class Evaluator:
    def evaluate(self,predictions,labels):
        raise NotImplementedError
class Visualizer:
    def visualize(self,results):
        raise NotImplementedError

# Concrete Products for classification
class LogisticRegressionModel(Model):
    def train(self,data):
        print("[LOG]: Training Logistic Regression on data")
        return [1,0,1,1] # fake prediction
class ConfusionMatrixEvaluator(Evaluator):
    def evaluate(self, predictions, labels):
        print("[LOG] Evaluating with Confusion Matrix")
        return {"TP": 2,"FP":1,"FN":0,"TN":1}
class ROCVisualizer(Visualizer):
    def visualize(self, results):
        print("[LOG]: Visualizing ROG Curve with results: ",results)
        return {"NTH":2.3,"RCT":5.7}

# Concrete Products for Regression
class LinearRegressionModel(Model):
    def train(self,data):
        print("[LOG]: Training Linear Regression on data")
        return [2.5,3.0,4.1] # Fake predictions
    
class RMSEEvaluatior(Evaluator):
    def evaluate(self, predictions, labels):
        print("[LOG]: Evaluating with RMSE")
        return {"RMSE":0.42}
class ScatterPlotVisualizer(Visualizer):
    def visualize(self, results):
        print("[LOG] Visualizing Scatter Plot with results: ",results)
        return {"TSC":7.0,"RNP":9.1}

# Abstract Factory
class ModelFactory:
    def create_model(self):
        raise NotImplementedError
    def create_evaluator(self):
        raise NotImplementedError
    def create_visualizer(self):
        raise NotImplementedError
    
# Concrete Factories
class ClassificationModelFactory(ModelFactory):
    def create_model(self):
        return LogisticRegressionModel()
    def create_evaluator(self):
        return ConfusionMatrixEvaluator()
    def create_visualizer(self):
        return ROCVisualizer()
    
class RegressionModelFactory(ModelFactory):
    def create_model(self):
        return LinearRegressionModel()
    def create_evaluator(self):
        return RMSEEvaluatior()
    def create_visualizer(self):
        return ScatterPlotVisualizer()
    

        
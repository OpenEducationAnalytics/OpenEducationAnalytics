
import abc
from enum import Enum

class ModelType(Enum):
    binary_classification = 1
    multiclass_classification = 2
    regression = 3

class ExplanationType(Enum):
    normal = 1
    ebm =2

class OEAModelInterface(metaclass=abc.ABCMeta):
    model_type = None
    explanation_type = None
    
    @classmethod
    def __subclasshook__(cls, subclass):

        if subclass.model_type == None or not (subclass.model_type in ModelType):
            print("Model Type Undefined or incorrect, Please set model_type in your class to a member of ModelType Enum - i.e. [model_type = ModelType.multiclass_classification]")
            return False

        return ((subclass.explanation_type in ExplanationType) and
                (subclass.model_type in ModelType) and
                hasattr(subclass, 'init_model') and 
                callable(subclass.init_model) and 
                hasattr(subclass, 'train') and 
                callable(subclass.train) and
                hasattr(subclass, 'test') and 
                callable(subclass.test) and
                hasattr(subclass, 'load_split_data') and 
                callable(subclass.load_split_data) and
                hasattr(subclass, 'save_model') and 
                callable(subclass.save_model) and 
                hasattr(subclass, 'register_model') and 
                callable(subclass.register_model) and
                hasattr(subclass, 'load_model') and 
                callable(subclass.load_model) and 
                callable(subclass.infer) or 
                NotImplemented)

    @abc.abstractmethod
    def init_model(self):
        """Initialize Model"""
        raise NotImplementedError

    @abc.abstractmethod
    def load_split_data(self):
        """Split Data sets into different blocks ?"""
        raise NotImplementedError

    @abc.abstractmethod
    def infer(self):
        """Infer using model"""
        raise NotImplementedError

    @abc.abstractmethod
    def train(self):
        """Train Model"""
        raise NotImplementedError

    @abc.abstractmethod
    def test(self):
        """Train Model"""
        raise NotImplementedError

    @abc.abstractmethod
    def save_model():
        """Save Model to a Path"""
        raise NotImplementedError

    @abc.abstractmethod
    def register_model():
        """Register Model to a repository"""
        raise NotImplementedError

    @abc.abstractmethod
    def load_model():
        """Load Model from an endpoint (?)"""
        raise NotImplementedError

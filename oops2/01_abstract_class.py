
import abc

class GetterSetter(object):
    __metaclass__= abc.ABCMeta

    @abc.abstractclassmethod
    def set_val(self,input):
        """set a value in the instance. """
        return
    
    @abc.abstractclassmethod
    def get_val(self):
        "Get and return a value from the instance. "
        return
    
    
import abc

class Operator (abc.ABC):

    _parser=None
    _args=None
    def __init__(self) -> None:
        return
    
    @abc.abstractmethod
    def build_argparser(self):
        return NotImplemented  

    @abc.abstractmethod
    def data_in(self):
        return NotImplemented
   
    @abc.abstractmethod
    def procress(self):
        return NotImplemented

    @abc.abstractmethod
    def data_out(self):
        return NotImplemented

    def run(self):
        self.build_argparser()
        self._args = self._parser.parse_args()
        self.data_in()
        self.procress()
        self.data_out()

if __name__ == '__main__':

    Operator().run()
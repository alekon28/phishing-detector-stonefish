""" Module contain a BaseAnalyzer class """

from abc import ABCMeta, abstractmethod
from urllib.parse import urlparse
import logging

from stonefish.models.analyzer import AnalyzerVerdictModel


class BaseAnalyzer(metaclass=ABCMeta):
    """ Base analyzer """
    name = 'Base analyzer'
    description = 'Analyzer for implements other analyzers'
    factor = 0  # Resulting points multiply with factor

    def __init__(self, url):
        """ Initialize """
        self.url = urlparse(url)

    @abstractmethod
    def execute(self) -> int:
        """ Method execute analyzer and return a points from 1 to 100 """
        raise NotImplementedError()

    def analyze(self) -> AnalyzerVerdictModel:
        """ Method execute analyzer and return a verdict """
        try:
            points = self.execute()
            return AnalyzerVerdictModel(
                points=points,
                factor=self.factor,
                result=self.factor * points,
                name=self.name,
                description=self.description,
                success=True
            )
        except Exception as err:
            logging.getLogger('__app__').warning(f'Analyzer "{self.__class__}" was crashed with exception: "{err}"',
                                                 exc_info=True)
            return AnalyzerVerdictModel(
                points=0,
                factor=self.factor,
                result=0,
                name=self.name,
                description=self.description,
                success=False
            )

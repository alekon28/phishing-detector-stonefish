""" Module contain models for analyzers """

from pydantic import BaseModel


class AnalyzerVerdictModel(BaseModel):
    """ Analyzer verdict model """
    points: int = None
    factor: float
    result: float = None
    success: bool
    name: str
    description: str


class AnalyzersOutcomeModel(BaseModel):
    """ Analyzer outcome model """
    points: int = None
    points_max: int = None
    result: float = None
    result_max: float = None
    score: float = None

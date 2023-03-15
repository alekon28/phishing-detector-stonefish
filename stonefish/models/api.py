""" Module contain api request models """
from typing import List
from uuid import UUID
from pydantic import BaseModel

from stonefish.models.analyzer import AnalyzerVerdictModel, AnalyzersOutcomeModel


class AnalyzeRequestModel(BaseModel):
    """ Analyze request model """
    url: str


class AnalyzeResponseModel(BaseModel):
    """ Analyze response model """
    session_id: UUID


class ResultRequestModel(BaseModel):
    """ Result request model """
    session_id: UUID


class ResultResponseModel(BaseModel):
    """ Result response model """
    url: str
    complete: bool
    details: List[AnalyzerVerdictModel]
    outcome: AnalyzersOutcomeModel

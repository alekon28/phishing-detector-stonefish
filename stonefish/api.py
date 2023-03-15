""" Module contain api endpoints """

from fastapi import APIRouter, BackgroundTasks

from stonefish.models.api import AnalyzeRequestModel, AnalyzeResponseModel, ResultRequestModel, ResultResponseModel
from stonefish.utils import Utils


router = APIRouter(prefix='/api/v1')


@router.post('/analyze', response_model=AnalyzeResponseModel)
def analyze(request: AnalyzeRequestModel, task: BackgroundTasks):
    """ The method starts the site analysis process """
    return Utils().run_analyzers(request.url, task)


@router.post('/result', response_model=ResultResponseModel)
def get_result(request: ResultRequestModel):
    """ The method returns the result of the analysis """
    return Utils().get_result(request.session_id)

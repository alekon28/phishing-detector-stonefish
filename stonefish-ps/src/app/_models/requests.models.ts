/* Module contains request data models */

import { IAnalyzersOutcomeModel, IAnalyzerVerdictModel } from "./data.models"

export interface IAnalyzeRequestModel {
    url: string
}

export interface IAnalyzeResponseModel {
    session_id: string
}

export interface IResultRequestModel {
    session_id: string
}

export interface IResultResponseModel {
    url: string
    complete: boolean
    details: IAnalyzerVerdictModel[]
    outcome: IAnalyzersOutcomeModel
}
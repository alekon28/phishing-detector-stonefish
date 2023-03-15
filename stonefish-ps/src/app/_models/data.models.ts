/* Module contains data models */

export interface IAnalyzerVerdictModel {
    points: number
    factor: number
    result: number
    success: boolean
    name: string
    description: string
}

export interface IAnalyzersOutcomeModel {
    points: number
    result: number
    points_max: number
    result_max: number
    score: number
}
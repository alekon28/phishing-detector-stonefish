import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { IAnalyzeResponseModel, IResultResponseModel } from '../_models/requests.models';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private httpClient: HttpClient) { }

  startAnalyze(url: string) {
    return this.httpClient.post<IAnalyzeResponseModel>(
      environment.apiEndpoint + '/analyze',
      {
        url: url
      }
    )
  }

  fetchResult(sessionId: string) {
    return this.httpClient.post<IResultResponseModel>(
      environment.apiEndpoint + '/result',
      {
        session_id: sessionId
      }
    )
  }
}

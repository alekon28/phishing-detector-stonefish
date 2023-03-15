import { Component } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { IAnalyzeResponseModel, IResultResponseModel } from './_models/requests.models';
import { ApiService } from './_services/api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent {
  title = 'Stonefish';

  constructor(private apiService: ApiService, private snackBar: MatSnackBar) {}

  results: IResultResponseModel = null
  analyzeProgressOn: boolean = false

  analyzeUrl(url: string) {
    this.apiService.startAnalyze(url).subscribe(
      {
        next: (value: IAnalyzeResponseModel) => {
          this.analyzeProgressOn = true
          setTimeout(() => this.fetchResults(value.session_id), 3000)
        },
        error: (err) => {
          this.analyzeProgressOn = false
          if (err?.error?.detail) {
            this.snackBar.open(err?.error?.detail, 'Ок', {duration: 5000})
          }
          else {
            this.snackBar.open('Что-то пошло не так :(', 'Ок', {duration: 5000})
          }
        }
        
      }
    )
  }

  fetchResults(sessionId: string): void {
    this.apiService.fetchResult(sessionId).subscribe(
      {
        next: (value: IResultResponseModel) => {
          this.results = value
          if (value.complete === false) {
            setTimeout(() => this.fetchResults(sessionId), 3000)
          }
          if (value.complete === true) {
            this.analyzeProgressOn = false
          }
        }
      }
    )
  }

  getVerdictColorClassName(score: number) {
    if (score >= 66) {
      return 'secure-text'
    } 
    else {
      if (score < 66 && score >= 33) {
        return 'suspect-text'
      }
      else {
        return 'unsecure-text'
      }
    }
  }

  getVerdictText(score: number) {
    if (score >= 66) {
      return 'Безопасно'
    } 
    else {
      if (score < 66 && score >= 33) {
        return 'Подозрительно'
      }
      else {
        return 'Фишинг'
      }
    }
  }
}

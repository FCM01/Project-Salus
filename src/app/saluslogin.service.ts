import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class SalusloginService {
  public url = " http://127.0.0.1:5000"
  public payload={};
  public response :any;
  constructor(public http: HttpClient) { }

  LoginCredentialSend(final_payload:any)
  {
    this.payload= JSON.stringify(final_payload) 
   return this.http.post(this.url+"/User/login",this.payload)
  }
}

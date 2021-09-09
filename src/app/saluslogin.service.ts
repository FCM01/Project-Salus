import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable, throwError } from 'rxjs';
import { catchError, map, retry } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class SalusloginService {
  public url = "http://127.0.0.1:5000/"
  public payload={};
  public response :any;
  public data:any;
  constructor(public http: HttpClient) { }

  LoginCredentialSend(final_payload:any)
  {
    // this.payload= JSON.stringify(final_payload) 
  //  return this.http.post(this.url+"/User/login",this.payload)
   const requestOptions: Object = {
    //If your response is text not json
    responseType: 'json'
  }    
  return this.http.post<any>(this.url+"/User/login", final_payload,requestOptions).pipe(map((data: any,error: any) => {
    if(data){
      return data;
    }
    else{
      return error;
    }
  })
  );
}
}
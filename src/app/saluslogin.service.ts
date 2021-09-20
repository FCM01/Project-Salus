import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable, throwError } from 'rxjs';
import { catchError, map, retry } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class SalusloginService {
  public url = "http://127.0.0.1:5000"
  public payload={};
  public response :any;
  public data:any;
  constructor(public http: HttpClient) { }

  SendForgetpasword(final_payload:any)
  {
    const requestOptions: Object = {
      //If your response is text not json
      responseType: 'json'
    }   
    return this.http.post<any>(this.url+"/forgot/passowrd1",final_payload,requestOptions).pipe(map((data: any,error: any) => {
      if(data){
        return data;
      }
      else{
        return error;
      }
    })
    );
  }

  SendVerificationCode(final_payload:any)
  {
    const requestOptions: Object = {
      //If your response is text not json
      responseType: 'json'
    }   
    return this.http.post<any>(this.url+"/forgot/passoword/send",final_payload,requestOptions).pipe(map((data: any,error: any) => {
      if(data){
        return data;
      }
      else{
        return error;
      }
    })
    );

  }

  TeacherSignUp(final_payload:any)
  {
    const requestOptions: Object = {
      //If your response is text not json
      responseType: 'json'
    }   
    return this.http.post<any>(this.url+"/Teacher/Signup",final_payload,requestOptions).pipe(map((data: any,error: any) => {
      if(data){
        return data;
      }
      else{
        return error;
      }
    })
    );

  }

  GetUsers(final_payload:any)
  {
    const requestOptions: Object = {
      //If your response is text not json
      responseType: 'json'
    }   
    return this.http.post<any>(this.url+"/retrieve/User",final_payload,requestOptions).pipe(map((data: any,error: any) => {
      if(data){
        return data;
      }
      else{
        return error;
      }
    })
    );

  }


  LoginCredentialSend(final_payload:any)
  {
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
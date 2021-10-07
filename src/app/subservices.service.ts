import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable, throwError } from 'rxjs';
import { catchError, map, retry } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class SubservicesService {
  public url = "http://127.0.0.1:5000"
  // public url ="http://143.160.105.127:5000"
  public payload={};
  public response :any;
  public data:any;

  constructor(public http: HttpClient) { }

  leaveComments(final_payload:any)
  {
    const requestOptions: Object = {
      //If your response is text not json
      responseType: 'json'
    }   
    return this.http.post<any>(this.url+"/Leave/comment",final_payload,requestOptions).pipe(map((data: any,error: any) => {
      if(data){
        return data;
      }
      else{
        return error;
      }
    })
    );
  }

  PurgeQRcodes(final_payload:any)
  {
    const requestOptions: Object = {
      //If your response is text not json
      responseType: 'json'
    }   
    return this.http.post<any>(this.url+"/Generate/Class/RegisterQR",final_payload,requestOptions).pipe(map((data: any,error: any) => {
      if(data){
        return data;
      }
      else{
        return error;
      }
    })
    );

  }
  RegisterClass(final_payload:any)
  {
    const requestOptions: Object = {
      //If your response is text not json
      responseType: 'json'
    }   
    return this.http.post<any>(this.url+"/Generate/Class/RegisterQR",final_payload,requestOptions).pipe(map((data: any,error: any) => {
      if(data){
        return data;
      }
      else{
        return error;
      }
    })
  );

  }
  GenerateEnterGroundsQR(final_payload:any)
  {
    const requestOptions: Object = {
      //If your response is text not json
      responseType: 'json'
    }   
    return this.http.post<any>(this.url+"/Enter/Grounds/QR",final_payload,requestOptions).pipe(map((data: any,error: any) => {
      if(data){
        return data;
      }
      else{
        return error;
      }
    })
  );
  }
  
  EnterGrounds(final_payload:any)
  {
    const requestOptions: Object = {
      //If your response is text not json
      responseType: 'json'
    }   
    return this.http.post<any>(this.url+"/Enter/Grounds",final_payload,requestOptions).pipe(map((data: any,error: any) => {
      if(data){
        return data;
      }
      else{
        return error;
      }
    })
  );


  }
  Markpresent(final_payload:any)
  {
    const requestOptions: Object = {
      //If your response is text not json
      responseType: 'json'
    }   
    return this.http.post<any>(this.url+"/Mark/Present",final_payload,requestOptions).pipe(map((data: any,error: any) => {
      if(data){
        return data;
      }
      else{
        return error;
      }
    })
  );


  }
  getComments()
  {
    const requestOptions: Object = {
      //If your response is text not json
      responseType: 'json'
    }   
    return this.http.get<any>(this.url+"/Retrieve/Messages",requestOptions).pipe(map((data: any,error: any) => {
      if(data){
        return data;
      }
      else{
        return error;
      }
    })
    );
  }

  
  GenerateToken(final_payload:any)
  {
    const requestOptions: Object = {
      //If your response is text not json
      responseType: 'json'
    }   
    return this.http.post<any>(this.url+"/Generate/Token",final_payload,requestOptions).pipe(map((data: any,error: any) => {
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



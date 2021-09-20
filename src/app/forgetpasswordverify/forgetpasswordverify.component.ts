import { Component, OnInit } from '@angular/core';
import { SalusloginService } from '../saluslogin.service';
import { Router } from '@angular/router';
import { EmailValidator, FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"

@Component({
  selector: 'app-forgetpasswordverify',
  templateUrl: './forgetpasswordverify.component.html',
  styleUrls: ['./forgetpasswordverify.component.css']
})
export class ForgetpasswordverifyComponent implements OnInit {
  public codeForm:any;
  public payload:any;
  public verifnumber = "nothings recieved";
  constructor(private responce:SalusloginService,private router:Router) { 
    this.codeForm =new FormGroup({
      "Code": new FormControl(Validators.required)
    });
  }

  ngOnInit(): void {
  }

  CheckCode(code:any){
    console.log(code)
    this.verifnumber = code ;
    console.log(this.verifnumber)
    this.payload={"data":{"verification_number":code}}
    this.responce.SendVerificationCode(this.payload)
      .subscribe(
        (data)=>{
          console.log(data)
          if (data["message"]=="sucess"){
            this.router.navigate(["/login"]);
          }
        }
      )

  }

}

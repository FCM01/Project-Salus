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

  //loading screen vaiables
  public wait =false;
  constructor(private responce:SalusloginService,private router:Router) { 
    this.codeForm =new FormGroup({
      "Code": new FormControl(Validators.required)
    });
  }

  ngOnInit(): void {
  }

  CheckCode(code:any){
    this.wait =true;
    this.verifnumber = code ;
    this.payload={"data":{"verification_number":code}}
    this.responce.SendVerificationCode(this.payload)
      .subscribe(
        (data)=>{
          if (data["message"]=="sucess"){
            this.wait=false;
            alert("Password Sent Check Your Email")
            this.router.navigate(["/login"]);
          }
        }
      )

  }

}

import { Component, OnInit } from '@angular/core';
import { SalusloginService } from '../saluslogin.service';
import { Router } from '@angular/router';
import { EmailValidator, FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"

@Component({
  selector: 'app-forgetpassword',
  templateUrl: './forgetpassword.component.html',
  styleUrls: ['./forgetpassword.component.css']
})
export class ForgetpasswordComponent implements OnInit {
  public sentemail=false;
  public forgotpasswordForm: any;
  public codeForm:any;
  public payload:any;
  //loading screen varible
  public wait:any;
  constructor(private responce:SalusloginService,private router:Router) { 
    this.forgotpasswordForm = new FormGroup({
      "Email": new FormControl(Validators.email),
    });

    this.codeForm =new FormGroup({
      "Code": new FormControl(Validators.required)
    });
  }

  ngOnInit(): void {
  }
  SetValue(email:string){
    this.wait = true;
    this.payload ={"data":{"email":email}};
    this.responce.SendForgetpasword(this.payload)
      .subscribe(
        (data)=>{
          console.log(data)

          if (data["token"]=="active")
          {
            this.wait =false;
            this.router.navigate(["/verify"]);
          }
          else{
            alert("Error");
          }

        }
      )

  }
}

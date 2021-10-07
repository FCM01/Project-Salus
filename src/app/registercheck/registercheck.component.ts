import { Component, OnInit } from '@angular/core';
import { NgModel } from '@angular/forms';
import { SubservicesService } from '../subservices.service';
import { Router } from '@angular/router';
import { FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"


@Component({
  selector: 'app-registercheck',
  templateUrl: './registercheck.component.html',
  styleUrls: ['./registercheck.component.css']
})
export class RegistercheckComponent implements OnInit {
  public signupForm : FormGroup;
  public payload  = {};
  public wait = false;
  public titleAlert1 :string ="This field is required"
  constructor(private sub :SubservicesService,private router: Router,private fb: FormBuilder) { 
    this.signupForm = fb.group(
      {
        "usernum": ['',Validators.required],
        "subject": ['',Validators.required],
        "register_class": ['',Validators.required],
    })
  }


  ngOnInit(): void {
  }

  setValue(post:any){
    this.wait = true;
    this.payload=
    {
      "data":{
        "user_number":post.usernum,
        "subject":post.subject,
        "register_class":post.register_class
      }
    }

    this.sub.Markpresent(this.payload)
      .subscribe(
        (data)=>{
          this.wait=false
          if (data["message"] == "successful")
          {
            console.log("done")
            this.router.navigate(["/login"])
          }

        }
      )
    
  }

}

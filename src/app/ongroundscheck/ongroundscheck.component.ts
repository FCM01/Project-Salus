import { Component, OnInit } from '@angular/core';
import { NgModel } from '@angular/forms';
import { SubservicesService } from '../subservices.service';
import { Router } from '@angular/router';
import { FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"

@Component({
  selector: 'app-ongroundscheck',
  templateUrl: './ongroundscheck.component.html',
  styleUrls: ['./ongroundscheck.component.css']
})
export class OngroundscheckComponent implements OnInit {
  public wait = false;
  public signupForm : FormGroup;
  public payload  = {};
  public titleAlert1 :string ="This field is required"
  constructor(private sub :SubservicesService,private router: Router,private fb: FormBuilder) { 
    this.signupForm = fb.group(
      {"usernum": ['',Validators.required],})
  }


  ngOnInit(): void {
  }

  setValue(post:any){
    this.wait = true;
    this.payload=
    {
      "data":{
        "user_number":post.usernum
      }
    }

    this.sub.EnterGrounds(this.payload)
      .subscribe(
        (data)=>{
          this.wait=false

          if (data["message"] == "successful")
          {
            this.router.navigate(["/login"])
          }

        }
      )
    
  }

}

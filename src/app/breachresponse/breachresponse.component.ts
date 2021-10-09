import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SubservicesService } from '../subservices.service';
import { FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"

@Component({
  selector: 'app-breachresponse',
  templateUrl: './breachresponse.component.html',
  styleUrls: ['./breachresponse.component.css']
})
export class BreachresponseComponent implements OnInit {
  //loading screen variable 
  public wait = false;
  //breach alarm varibales
  public breachForm : FormGroup;
  public breach_number :any;
  public breach_type:any;
  public quadrent:any;
  public titleAlert1 :string ="This field is required"
  constructor(private sub:SubservicesService,private router: Router,private fb: FormBuilder) {
    this.breachForm = this.fb.group({
      "breach_number": ['',Validators.required],
      "validate":""
    })
   }

  ngOnInit(): void {
    //get breach
    this.wait = true
    this.sub.getBreach()
      .subscribe(
        (data)=>{
          this.wait = false;
          console.log(data)
          if(data != ""){
            this.breach_number =data["response"]["breach_number"]
            this.breach_type = data["response"]["breach_type"]
            this.quadrent = data["response"]["quadrant"]
          }
        }
      )
  }

  Respond(post:any){
    console.log(post.breach_number)
    let payload ={
      "data":{
        "breach_number":post.breach_number
      }
    }
    this.sub.UpdateStatus(payload)
      .subscribe(
        (data)=>{
          alert("Response has been sent")
          console.log(data)
          
        }
      )
  }
  
}

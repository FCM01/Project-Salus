import { Component, OnInit } from '@angular/core';
import { SalusloginService } from '../saluslogin.service';
import { Router } from '@angular/router';
import { FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"

@Component({
  selector: 'app-breachalarm',
  templateUrl: './breachalarm.component.html',
  styleUrls: ['./breachalarm.component.css']
})
export class BreachalarmComponent implements OnInit {
  public quadrant:any;
  public wait = false;
  public breachtype = "";
  public breach:FormGroup;
  //session variables
  public user_number:any;
  public user_type :any;
  public data :any ;
  public titleAlert1 :string ="This field is required"
  constructor(private log :SalusloginService,private router: Router,private fb: FormBuilder) {
    this.breach =this.fb.group({
      "type": ['', Validators.required],
    })
   }

  ngOnInit(): void {
    //Sessions
    const user_profile_recieved = (localStorage.getItem('global_user_number'));
    this.data = user_profile_recieved
    this.data= JSON.parse(this.data);
    this.user_type = this.data["user_type"];
    this.user_number =this.data["user_number"];
  }
  
  myDate = new Date();

  
  getDate(val1: Date)
  {
    console.log(val1)
    this.myDate = val1;
  }

  MakeBreach(post:any)
  {
    this.wait = true;
    
    let payload ={
       "data":{
        "user_number" :this.user_number,
        "quadrant" :this.quadrant,
        "breach_type" :post.type
       }
    }
    console.log("data==>",payload)

    this.log.MakeBreachAlarm(payload)
      .subscribe(
        (data)=>{
          this.wait = false;
          console.log(this.user_type)
          if(this.user_type=="teacher")
          {
            this.router.navigate(['/teacherdash']) 
          }
          else if(this.user_type=="domestic")
          { 
            this.router.navigate(['/domesticdash'])
          }
          else if(this.user_type=="security")
          {
            this.router.navigate(['/securitydash'])
          }
          else if(this.user_type=="admin")
          {
            this.router.navigate(['/admindash'])
          }
        }
      )

  } 


  Getquadrant(q: string){

    if(q == "Q1"){
      this.quadrant = "Quadrant 1";
      console.log(this.quadrant)
    }

    else if (q == "Q2"){
      this.quadrant = "Quadrant 2";
      console.log(this.quadrant)
    }

    else if(q == "Q3"){
      this.quadrant = "Quadrant 3";
      console.log(this.quadrant)
    }

    else if (q == "Q4"){
      this.quadrant = "Quadrant 4";
      console.log(this.quadrant)
    }



  }

}

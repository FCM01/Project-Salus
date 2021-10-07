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
  public user_number:any;
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
    this.user_number = JSON.parse(this.data);
  }
  
  myDate = new Date();

  
  getDate(val1: Date)
  {
    console.log(val1)
    this.myDate = val1;
  }

  

  getBreachType(post:any)
  {
    this.wait = true;
    let payload ={
       "data":{
        "user_number" :this.user_number["user_number"],
        "quadrant" :this.quadrant,
        "breach_type" :post.type
       }
    }

    this.log.MakeBreachAlarm(payload)
      .subscribe(
        (data)=>{
          this.wait = false;
          console.log(data)
          if (this.user_number=="student"){
            this.router.navigate(['/studentdash'])
          }
          else if(this.user_number=="teacher")
          {
            this.router.navigate(['/teacherdash']) 
          }
          else if(this.user_number=="domestic")
          { 
            this.router.navigate(['/domesticdash'])
          }
          else if(this.user_number=="security")
          {
            this.router.navigate(['/securitydash'])
          }
          else if(this.user_number=="visitor")
          {
            this.router.navigate(['/visitordash'])
          }
          else if(this.user_number=="admin")
          {
            this.router.navigate(['/admindash'])
          }
        }
      )

  } 


  Getquadrant(q: string){

    if(q == "Quadrant 1"){
      this.quadrant = q;
      console.log(this.quadrant)
    }

    else if (q == "Quadrant 2"){
      this.quadrant = q;
      console.log(this.quadrant)
    }

    else if(q == "Quadrant 3"){
      this.quadrant = q;
      console.log(this.quadrant)
    }

    else if (q == "Quadrant 4"){
      this.quadrant = q;
      console.log(this.quadrant)
    }



  }

}

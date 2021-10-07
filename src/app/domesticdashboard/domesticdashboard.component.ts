import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SalusloginService } from '../saluslogin.service';
import { FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"

@Component({
  selector: 'app-domesticdashboard',
  templateUrl: './domesticdashboard.component.html',
  styleUrls: ['./domesticdashboard.component.css']
})
export class DomesticdashboardComponent implements OnInit {
  public user_profile:any;
  public data :any ;
 
  constructor(private log :SalusloginService,private router: Router,private fb: FormBuilder) { 
 
  }

  ngOnInit(): void {
    const user_profile_recieved = (localStorage.getItem('user_profile'));
    this.data = user_profile_recieved
    this.user_profile = JSON.parse(this.data);
  }
  



}

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

  public User:any;
 
  constructor(private log :SalusloginService,private router: Router,private fb: FormBuilder) { 
 
  }

  ngOnInit(): void {
    sessionStorage.getItem('id');
  
  }
  



}

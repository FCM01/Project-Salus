import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { ContactComponent } from './contact/contact.component';
import { BreachalarmComponent } from './breachalarm/breachalarm.component';
import {HttpClientModule} from '@angular/common/http';
import {FormsModule, ReactiveFormsModule}from "@angular/forms";
import { RegistercheckComponent } from './registercheck/registercheck.component';
import { StudentsuComponent } from './studentsu/studentsu.component';
import { StaffsuComponent } from './staffsu/staffsu.component';
import { SecuritysuComponent } from './securitysu/securitysu.component';
import { ForgetpasswordComponent } from './forgetpassword/forgetpassword.component';
import { StudentdasboardComponent } from './studentdasboard/studentdasboard.component';
import { TeacherdashbaoardComponent } from './teacherdashbaoard/teacherdashbaoard.component';
import { DomesticdashboardComponent } from './domesticdashboard/domesticdashboard.component';
import { SecuritydashboardComponent } from './securitydashboard/securitydashboard.component';
import { AdmindashboardComponent } from './admindashboard/admindashboard.component';
import { VisitordashboardComponent } from './visitordashboard/visitordashboard.component';
import { ForgetpasswordverifyComponent } from './forgetpasswordverify/forgetpasswordverify.component';
import { VisitorssuComponent } from './visitorssu/visitorssu.component';
import { DomesticsuComponent } from './domesticsu/domesticsu.component';
import { AdminsuComponent } from './adminsu/adminsu.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    HomeComponent,
    LoginComponent,
    SignupComponent,
    ContactComponent,
    BreachalarmComponent,
    RegistercheckComponent,
    StudentsuComponent,
    StaffsuComponent,
    SecuritysuComponent,
    ForgetpasswordComponent,
    StudentdasboardComponent,
    TeacherdashbaoardComponent,
    DomesticdashboardComponent,
    SecuritydashboardComponent,
    AdmindashboardComponent,
    VisitordashboardComponent,
    ForgetpasswordverifyComponent,
    VisitorssuComponent,
    DomesticsuComponent,
    AdminsuComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    ReactiveFormsModule,
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

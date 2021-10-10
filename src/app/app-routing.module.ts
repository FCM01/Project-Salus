import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BreachalarmComponent } from './breachalarm/breachalarm.component';
import { ContactComponent } from './contact/contact.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { StaffsuComponent } from './staffsu/staffsu.component';
import { SecuritysuComponent } from './securitysu/securitysu.component';
import { StudentsuComponent } from './studentsu/studentsu.component';
import { ForgetpasswordComponent } from './forgetpassword/forgetpassword.component';
import { StudentdasboardComponent } from './studentdasboard/studentdasboard.component';
import { SecuritydashboardComponent } from './securitydashboard/securitydashboard.component';
import { VisitordashboardComponent } from './visitordashboard/visitordashboard.component';
import { TeacherdashbaoardComponent } from './teacherdashbaoard/teacherdashbaoard.component';
import { DomesticdashboardComponent } from './domesticdashboard/domesticdashboard.component';
import { ForgetpasswordverifyComponent } from './forgetpasswordverify/forgetpasswordverify.component';
import { DomesticsuComponent } from './domesticsu/domesticsu.component';
import { VisitorssuComponent } from './visitorssu/visitorssu.component';
import { AdminsuComponent } from './adminsu/adminsu.component';
import { AdmindashboardComponent } from './admindashboard/admindashboard.component';
import { RegistercheckComponent } from './registercheck/registercheck.component';
import { OngroundscheckComponent } from './ongroundscheck/ongroundscheck.component';
import { BreachresponseComponent } from './breachresponse/breachresponse.component';
import { StudenteditComponent } from './studentedit/studentedit.component';
import { TeachereditComponent } from './teacheredit/teacheredit.component';
import { AdmineditComponent } from './adminedit/adminedit.component';
import { SecurityeditComponent } from './securityedit/securityedit.component';
import { DomesticeditComponent } from './domesticedit/domesticedit.component';
import { VisitoreditComponent } from './visitoredit/visitoredit.component';

const routes: Routes = [
  {path:"",component :HomeComponent},
  {path:"contact",component :ContactComponent},
  {path:"login",component:LoginComponent},
  {path:"signup",component:SignupComponent},
  {path:"studentsignup",component:StudentsuComponent},
  {path:"staffsignup",component:StaffsuComponent},
  {path:"securitysignup",component:SecuritysuComponent},
  {path:"breach",component:BreachalarmComponent},
  {path:"forgotpassword",component:ForgetpasswordComponent},
  {path:"studentdash",component:StudentdasboardComponent},
  {path:"visitordash",component:VisitordashboardComponent},
  {path:"securitydash",component:SecuritydashboardComponent},
  {path:"domesticdash",component:DomesticdashboardComponent},
  {path:"teacherdash",component:TeacherdashbaoardComponent},
  {path:"verify",component:ForgetpasswordverifyComponent},
  {path:"visitorsignup",component:VisitorssuComponent},
  {path:"domesticsignup",component:DomesticsuComponent },
  {path:"adminsu",component:AdminsuComponent},
  {path:"admindash",component:AdmindashboardComponent},
  {path:"registercheck",component:RegistercheckComponent},
  {path:"ongroundscheck",component:OngroundscheckComponent},
  {path:"breachresponse",component:BreachresponseComponent},
  {path:"studentedit",component:StudenteditComponent},
  {path:"teacheredit",component:TeachereditComponent},
  {path:"domesticedit",component:DomesticeditComponent},
  {path:"securityedit",component:SecurityeditComponent},
  {path:"visitoredit",component:VisitoreditComponent},
  {path:"adminedit",component:AdmineditComponent},


  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SalusloginService } from '../saluslogin.service';
import { SubservicesService } from '../subservices.service';
import { FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"

@Component({
  selector: 'app-admindashboard',
  templateUrl: './admindashboard.component.html',
  styleUrls: ['./admindashboard.component.css']
})
export class AdmindashboardComponent implements OnInit {
  public databaseForm: FormGroup;
  //breach varaiables 
  public breach_status = ""
  public breach_number :any;
  public breach_type:any;
  public quadrent:any;
  public message_alert = false;
  public show_make_breach =true;
  //reply variables 
  public show_reply_section=false;
  public show_message = true;
  public current_message_number=""
  public current_message_name=""
  public current_message_message=""
  //qr loading screen
  public wait = false;

  //form and other variables
  public payload = {};
  public num = 0;
  public data :any ;
  public datetime:any;
  public user_profile:any;
  public messages =null;
  public userarray=null;
  public status:any;
  public databaseselected:any; 
  public titleAlert1 :string ="This field is required"
  //edit variables 
  public edit_user_type:any;
  public editForm:FormGroup;

  //toolbar variable
 public toolbar_show:any;
 public toolbar_default = true;
 public toolbar_report = false;
 public toolbar_message = false;
 public toolbar_endday = false;


 //report variables
 public report_data :any;

  list1 = [
    { text: 'Admin', selected: false, value:"admin"},
    { text: 'Domestic', selected: false, value:"domestic"},
    { text: 'Security', selected: false, value:"security"},
    { text: 'Student', selected: false,  value:"student"},
    { text: 'Teacher', selected: false,  value:"teacher"},
    { text: 'Visitor', selected: false,  value:"visitor"}
  ];

  
  constructor(private log :SalusloginService,private router: Router,private fb: FormBuilder,private sub :SubservicesService) { 
    this.databaseForm = fb.group(
      { "database_name":['',Validators.required],})

    this.editForm =fb.group(
      {"user_number":['',Validators.required]}
    )
    
  }

  ngOnInit(): void {
    //date area

    this.datetime = new Date();
   
    //Sessions
    const user_profile_recieved = (localStorage.getItem('user_profile'));
    this.data = user_profile_recieved
    this.user_profile = JSON.parse(this.data);

    //set user_number for breach alram
    let session_payload  = {
      "user_number":this.user_profile["admin_number"],
      "user_type":"admin" 
    }
    localStorage.setItem('global_user_number',JSON.stringify(session_payload));
    this.sub.getComments()
    .subscribe(
      (data)=>
      {
        this.messages  = data["response"]

      }
    )
    //breach status 
    this.sub.getBreach()
      .subscribe(
        (data)=>{
          if(data != ""){
            this.message_alert = true
            this.show_make_breach =false
              this.breach_number =data["response"]["breach_number"]
              this.breach_type = data["response"]["breach_type"]
              this.quadrent = data["response"]["quadrant"]
            if (data["response"]["status"]== "onroute"){
              this.breach_status = "AID is on the Way" 
            }
            
          }
        }
      )

    //fecth report numbers 
    this.sub.NumberOfUsers()
    .subscribe(
      (data)=>{
        this.report_data = data
      }
    )

   
  }
  public toggleSelection(item:any, _list:any) {
    item.selected = !item.selected;
    this.databaseselected= item.value;

  }

  toolbarControlEdit()
  {
    this.toolbar_show="edit"
    this.toolbar_default =false;
    this.toolbar_report =false;
    this.toolbar_endday =false;
  }

  toolbarControlHome()
  {
    this.toolbar_show=""
    this.toolbar_default =true;
    this.toolbar_report =false;
    this.toolbar_endday =false;
  }
  toolbarControlReport()
  {
    this.toolbar_report =true;
    this.toolbar_default=false;
    this.toolbar_show="";
    this.toolbar_endday =false;

  }

  toolbarControlMessages()
  {
    this.toolbar_message = true;
    this.toolbar_report =false;
    this.toolbar_default=false;
    this.toolbar_show="";
    this.toolbar_endday =false;

  }
  toolbarControlPurge()
  {
    this.toolbar_endday =true;
    this.toolbar_message = false;
    this.toolbar_report =false;
    this.toolbar_default=false;
    this.toolbar_show="";

  }

  Emptylogs(){
    console.log("working")
    this.sub.DeleteDaily()
      .subscribe(
        (data)=>{
          if (data["message"]=="deleted"){
            alert("Daily logs deleted")
          }
         

        }
      )

  }
  Deletelocal_logs(){
    this.sub.DeleteLocalLogs()
      .subscribe(
        (data)=>{
          if (data["message"]=="deleted"){
           alert("Purge complete")
            
          }
          
        }
      )

 }
  deletUser(name:any,surname:any)
  {
    console.log ("type user ==>",this.databaseselected)
    this.payload ={
      "data":{
      "name":name,
      "surname":surname,
      "user_type":this.databaseselected
      }
    }
    console.log(this.payload)
    this.log.DeleteUser(this.payload)
      .subscribe(
        (data)=>
        {
          if(data["message"]=="deleted")
          {

            alert("User has been deleted")
            location.reload()

          }
        }
      )

  }
  GenrateQR(){
    this.wait = true;
    let user_number  = this.user_profile["admin_number"]
    console.log(user_number)
    let payload = {
      "data":{
        "user_number":user_number
      }
    }
    this.sub.GenerateEnterGroundsQR(payload)
      .subscribe(
        (data)=>{
          if (data != ""){
            this.wait=false;
          }
        }
      )


}

GenerateQR()
{
  this.wait = true;
  let user_number  = this.user_profile["admin_number"]
  let payload = {
    "data":{
      "user_number":user_number
    }
  }
  this.sub.RegisterClass(payload)
    .subscribe(
      (data)=>{
        if (data != ""){
          this.wait=false;
        }
        
      }
    )
}



  deleteBreach()
  {
    let payload =
    {
      "data":{
        "breach_number":this.breach_number
      }
    }

    this.sub.DeleteBreachAlarm(payload)
      .subscribe(
        (data)=>{
          if (data["status"]==200){
          
          this.message_alert = false
          }
        }
      )

  }
  deleteMessage(message_number:any)
  {
    
    let payload =
    {
      "data":{
        "message_number":message_number
      }
    }
    this.sub.DeleteMessage(payload)
      .subscribe(
        (data)=>{
          if (data["status"]==200){
            alert("Message Deleted")
            location.reload();
           
          }
        }
      )

  }

  setValues()
  {
    this.payload = {
      "data":{
        "database_name":this.databaseselected
      }
    }
    this.log.GetUsers(this.payload)
      .subscribe(
        (data)=>{

          if (data["response"] != "")
          {
            this.userarray = data["response"]
          }

        }
      )
      console.log (this.userarray)

}

ReplyShow(name:any,message_number:any,message:any){
  this.show_reply_section = true;
  this.show_message =false;
  //

  this.current_message_message = message;
  this.current_message_name =name;
  this.current_message_number =message_number;
}
ReplyHide(){
  this.show_reply_section=false;
  this.show_message =true;
}
GenerateToken()
{
  this.status="Generating";
  let user_number =this.user_profile["admin_number"]
  this.payload={
    "data":{
      "user_number":user_number,
      "user_type":"admin"
    }
  }
  this.sub.GenerateToken(this.payload)
    .subscribe(
      (data)=>
      {
        if (data["status"]=="200")
        {
          this.status = "TOKEN CReAtED AND SENT "
        }
        console.log(data)
      }
    )
  


  }
  //edit function sessions 
  public toggleSelectionEdit(item:any, _list:any) {
    item.selected = !item.selected;
    this.edit_user_type= item.value;

  }
  EditUser(user:any){
   
    let user_number ="";
    //get user number
    if (user["staff_number"]){
      user_number= user["staff_number"]
      console.log(user_number)
    }
    if (user["student_number"]){
      user_number= user["student_number"]
      console.log(user_number)
    }
    if (user["visitor_number"]){
      user_number= user["visitor_number"]
      console.log(user_number)
    }
    if (user["admin_number"]){
      user_number= user["admin_number"]
      console.log(user_number)
    }
    //making a session
    let session_payload ={
      "user_number":user_number
    }
    if (this.databaseselected =="student"){
      localStorage.setItem('user_edit_profile',JSON.stringify(session_payload));
      this.router.navigate(["/studentedit"]) 
    }
    else if (this.databaseselected =="security"){
      localStorage.setItem('user_edit_profile',JSON.stringify(session_payload));
      this.router.navigate(["/securityedit"]) 

    }
    else if (this.databaseselected =="teacher"){
      localStorage.setItem('user_edit_profile',JSON.stringify(session_payload));
      this.router.navigate(["/teacheredit"]) 

    }
    else if (this.databaseselected =="domestic"){ 
      localStorage.setItem('user_edit_profile',JSON.stringify(session_payload));
      this.router.navigate(["/domesticedit"]) 

    }
    else if (this.databaseselected =="admin"){
      localStorage.setItem('user_edit_profile',JSON.stringify(session_payload));
      this.router.navigate(["/adminedit"]) 

    }
    else if (this.databaseselected =="visitor"){
      localStorage.setItem('user_edit_profile',JSON.stringify(session_payload));
      this.router.navigate(["/visitoredit"]) 

    }
    

  }

  replyMessage(message_number:any ,message:any){

    let payload ={
      "data":{
        "message_number":message_number ,
        "response_message": message
      }
    }
    console.log(payload)
    this.sub.SendReponse(payload)
      .subscribe(
        (data)=>{
          if (data["message"] != "successful"){
            this.show_reply_section=false;
            this.show_message =true;

          }
        }
      )

  }

}



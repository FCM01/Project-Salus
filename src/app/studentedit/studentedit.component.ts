import { Component, OnInit } from '@angular/core';
import { SalusloginService } from '../saluslogin.service';
import { SubservicesService } from '../subservices.service';
import { Router } from '@angular/router';
import { FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"

@Component({
  selector: 'app-studentedit',
  templateUrl: './studentedit.component.html',
  styleUrls: ['./studentedit.component.css']
})
export class StudenteditComponent implements OnInit {
  //Session varibale
  public user_number:any;
  public edit_profile:any;
  public edit_data:any;

  //edit variables
  public edit_payload:any;
  public editForm:FormGroup;
  public wait = false;
  public titleAlert1 :string ="This field is required";
  public titleAlert2 :string ="Please enter in an password that is 8 charaters long"

  constructor(private sub:SubservicesService,private log :SalusloginService,private router: Router,private fb: FormBuilder) {
    this.editForm = fb.group({
      "name": [''],
      "surname": [''],
      "id_number": [''],
      "date_of_birth": [''],
      "register_class": [''],
      "email": [''],
      "password": ['', Validators.compose([Validators.maxLength(12)])],
      "cnr": [''],
      "address": [''],
      "city": [''],
      "pcode": [''],
      "pg_name": [''],
      "pg_surname": [''],
      "pg_id_number": [''],
      "pg_cnum": [''],
      "pg_email": [''],
      "validate": ''
      
    })
   }

  ngOnInit(): void {
 
    //edit sessions
    const user_edit_profile_recieved = (localStorage.getItem('user_edit_profile'));
    this.edit_data = user_edit_profile_recieved 
    this.edit_profile = JSON.parse(this.edit_data);
    
    this.user_number= this.edit_profile["user_number"]
    let get_user_payload ={
      "data":{
        "user_number":this.user_number
      }
    }
    this.sub.GetUser(get_user_payload)
      .subscribe(
        (data)=>{
          console.log("data recieved",data["user"])
          this.edit_payload = data["user"];
        }
      )

  }
  EditForm(post:any){
    this.wait = true;
    let name = "";
    let surname = "";
    let id_number = "";
    let date_of_birth = "";
    let studentnum = "";
    let register_class= "";
    let email = "";
    let password = "";
    let address="";
    let cnr = "";
    let city = "";
    let pcode = "";
    let pg_name = "";
    let pg_surname = "";
    let pg_id_number= "";
    let pg_cnum= "";
    let pg_email= "";



    if(post.name == ""){
      name =this.edit_payload["name"];
    }
    else{
      name =post.name;
    }

    if(post.surname == ""){
      surname =this.edit_payload["surname"];
    }
    else{
      surname =post.surname;
    }
    
    if(post.id_number == ""){
      id_number = this.edit_payload["id_number"];
    }
    else{
      id_number =post.id_number;
    }

    if(post.date_of_birth == ""){
      date_of_birth =this.edit_payload["date_of_birth"];
    }
    else{
      date_of_birth =post.date_of_birth;
    }

  
    studentnum =this.user_number;
  

    if(post.register_class == ""){
      register_class =this.edit_payload["register_class"];
    }
    else{
      register_class =post.register_class;
    }

    if(post.email == ""){
      email =this.edit_payload["email"];
    }
    else{
      email =post.email;
    }

    if(post.password == ""){
      password =this.edit_payload["password"];
    }
    else{
      password =post.password;
    }
    if(post.cnr == ""){
      cnr = this.edit_payload["phone_number"];
    }
    else{
      cnr = post.cnr;
    }
    if(post.city == ""){
      city =this.edit_payload["city"];
    }
    else{
      city =post.city;
    }
    if(post.pcode == ""){
      pcode =this.edit_payload["pcode"];
    }
    else{
      pcode =post.pcode;
    }
    if(post.address == ""){
      address =this.edit_payload["address"];
    }
    else{
      address =post.address;
    }
    if(post.pg_name == ""){
      pg_name =this.edit_payload["pg_name"];
    }
    else{
      pg_name =post.pg_name;
    }
    if(post.pg_surname == ""){
      pg_surname =this.edit_payload["pg_surname"];
    }
    else{
      pg_surname =post.pg_surname;
    }

    if(post.pg_id_number == ""){
      pg_id_number =this.edit_payload["pg_id_number"];
    }
    else{
      pg_id_number =post.pg_id_number;
    }
    if(post.pg_cnum== ""){
      pg_cnum =this.edit_payload["pg_phone_number"];
    }
    else{
      pg_cnum =post.pg_cnum;
    }
    if(post.pg_email == ""){
      pg_email =this.edit_payload["pg_email"];
    }
    else{
      pg_email =post.pg_email;
    }

    //Send data 
    let payload ={
      "data":{
        "user_number":this.user_number,
        "user_profile":{
                "name":name,
                 "surname":surname,
                "id_number":id_number,
                "date_of_birth":date_of_birth,
                "email":email,
                "phone_number":cnr,
                "address":address,
                "city":city,
                "pcode":pcode,
                "password":password,
                "student_number":studentnum,
                "register_class":register_class,
                "pg_name":pg_name,
                "pg_surname":pg_surname,
                "pg_id_number":pg_id_number,
                "pg_cnum": pg_cnum,
                "pg_email":pg_email,
        }
      }

  }
  this.sub.EditUser(payload)
    .subscribe(
      (data)=>{
        if (data["message"]=="successful"){
          this.wait =false
          alert("User has been updated")
          this.router.navigate(["/studentdash"])

        }
      }
    )

}
}
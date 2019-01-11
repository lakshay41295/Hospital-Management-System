import cx_Oracle
import datetime
report_no=1
patient_count_morning=0
patient_count_evening=0
patient_count_morning1=0
patient_count_evening1=0
patient_count_morning2=0
patient_count_evening2=0
patient_count_morning3=0
patient_count_evening3=0
appointment_no_morning=1
appointment_no_evening=2
appointment_no_morning1=1
appointment_no_evening1=1
appointment_no_morning2=1
appointment_no_evening2=1
appointment_no_morning3=1
appointment_no_evening3=1
consultantfees=600
adm_charges=1200
labtest=300
no_of_wards=3
no_of_beds=15



class Registration:
    def __init__(self,UserId,UserName,Password,Email,MobileNo,dob,age,gender,height,weight,designation,specialist,prescription,labtest,admit):
        self.UserId=UserId
        self.UserName=UserName
        self.Password=Password
        self.Email=Email
        self.MobileNo=MobileNo
        self.dob=dob
        self.age=age
        self.gender=gender
        self.height=height
        self.weight=weight
        self.designation=designation
        self.specialist=specialist
        self.prescription=prescription
        self.labtest=labtest
        self.admit=admit
class Schedule:
    def __init__(self,userid,type_1,timein,timeout,duration):
        self.userid=userid
        self.type_1=type_1
        self.timein=timein
        self.timeout=timeout
        self.duration=duration
    def print_schedule(self):
        print("Shift:",self.type_1)
        print("In Time:",self.timein)
        print("Out Time",self.timeout)

class Appointment(Registration):
    def __init__(self,UserId,UserName,Password,Email,MobileNo,dob,age,gender,height,weight,designation,specialist,prescription,labtest,admit,type_1,AppnNo):
        Registration.__init__(self,UserId,UserName,Password,Email,MobileNo,dob,age,gender,height,weight,designation,specialist,prescription,labtest,admit)
        self.type=type_1
        self.AppnNo=AppnNo
    def print_appointment(self):
        print("UserId:",self.UserId)
        print("UserName:",self.UserName)
        print("Email:", self.Email)
        print("Mobile Number:", self.MobileNo)
        print("Date of Birth",self.dob)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Height:",self.height)
        print("Weight", self.weight)
        print("Appointment Shift:",self.type)
        print("Appointment Number:", self.AppnNo)
        
        



class LabTest(Registration):
    def __init__(self,UserId,UserName,Password,Email,MobileNo,dob,age,gender,height,weight,designation,specialist,prescription,labtest,admit,collect_sample,report,reportno):
        Registration.__init__(self,UserId,UserName,Password,Email,MobileNo,dob,age,gender,height,weight,designation,specialist,prescription,labtest,admit)
        self.collect_sample=collect_sample
        self.report=report
        self.reportno=reportno
    def print_labtest(self):
        print("UserId:",self.UserId)
        print("UserName:",self.UserName)
        print("Email:", self.Email)
        print("Mobile Number:", self.MobileNo)
        print("Date of Birth",self.dob)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Height:",self.height)
        print("Weight", self.weight)
        print("Report NO:",self.reportno)
        print("Report",self.report)
        

class Admit (Registration):
    def __init__(self,UserId,UserName,Password,Email,MobileNo,dob,age,gender,height,weight,designation,specialist,prescription,labtest,admit,wardno, bedno):
        Registration.__init__(self,UserId,UserName,Password,Email,MobileNo,dob,age,gender,height,weight,designation,specialist,prescription,labtest,admit)

        self.wardno=wardno
        self.bedno=bedno

    def print_inventory(self):
        print("UserId:",self.UserId)
        print("UserName:",self.UserName)
        print("Email:", self.Email)
        print("Mobile Number:", self.MobileNo)
        print("Date of Birth",self.dob)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Height:",self.height)
        print("Weight", self.weight)
        print("Ward No:",self.wardno)
        print("Bed No:",self.bedno)



        

   
def personal_details():
    print("Personal Details")
    id1=int(input("1. ID (Random No ):"))
    id2=str(id1)
    userid="S"+id2
    name=input("2.Username:")
    password=input("3.Password:")
    email=input("4.Email:")
    mobile=int(input("5.Mobile:"))
    dob= input('6.Enter a dob in DD-MON-YYYY format')
    age=int(input("7.Age:"))
    gender=input("8.Gender:")
    height=(input("8.Height:"))
    weight=input("10.Weight:")
    designation=input("11.Designation(Doctor, Patient,Labotorist)")
    specialist=input("12.Specialist(if patient then none)")
    cur.execute("Insert into Registration Values(:param1,:param2,:param3,:param4,:param5,:param6,To_Date(:param7,'DD-MON-YYYY'),:param8,:param9,:param10,:param11,:param12)",{'param1':userid,'param2':name,'param3':password,'param4':email,'param5':mobile,'param6':gender,'param7':dob,'param8':height,'param9':weight,'param10':designation,'param11':age,'param12':specialist})
    #con.commit()
    print("Your UserID:",userid)
    print("Your Password:",password)

def doctor_functionality():
    username=input("Enter the UserName :")
    password=input("Enter the password:")
    cur.execute("Select Password from Registration  where Userid=:param1",{'param1':username});
    rows=cur.fetchall()
    x=rows[0][0]
    if(password==x):
        print("1. Scedule")
        print("2. Appointments")
        print("3. Prescription")
        print("4. Quit")
        input1=int(input("Enter the choice "))
        if(input1==1):
            cur.execute("Select * from Schedule where UserID= :param1",{'param1':username})
            rows=cur.fetchall()
            u=rows[0][0]
            w=rows[0][1]
            x=rows[0][2]
            y=rows[0][3]
            z=rows[0][4]
            a=rows[1][0]
            b=rows[1][1]
            c=rows[1][2]
            d=rows[1][3]
            e=rows[1][4]
            sch1=Schedule(u,w,x,y,z)
            sch1.print_schedule()
            sch2=Schedule(a,b,c,d,e)
            sch2.print_schedule()
        if(input1 == 2):
            input_6=input("Enter the shift")
            cur.execute("Select PatientCount from Schedule where UserID =:param1 And Type=:param2",{'param1':username,'param2':input_6})
            print(cur.fetchall())
        if(input1 == 3):
            patientid=input("Enter Patient Id:")
            cur.execute("Select * from Registration where UserId=:param1",{'param1':patientid})
            rows1=cur.fetchall()
            a=rows1[0][1]
            b=rows1[0][3]
            c=rows1[0][4]
            d=rows1[0][5]
            e=rows1[0][6]
            f=rows1[0][7]
            g=rows1[0][8]
            h=rows1[0][10]
            print("1.Name :",a)
            print("2.Email Id :",b)
            print("3.Mobile :" ,c)
            print("4.Gender",d)
            print("5.Date of Birth :",e)
            print("6.Height :",f)
            print("7.Weight :",g)
            print("8.Age: ",h)
            prescription =input("9.Prescription :")
            labtest= input("10. Lab Test:")
            admit=input("11. Admit:")
            cur.execute(" UPDATE Registration SET Prescription = :param1, Labtest=:param2, Admit=:param3 WHERE UserId = :param4",{'param1':prescription,'param2':labtest,'param3':admit,'param4':patientid})
            #con.commit()


def patient_functionality():
    username=input("Enter the UserName :")
    password=input("Enter the password:")
    cur.execute("Select Password from Registration  where Userid=:param1",{'param1':username});
    rows=cur.fetchall()
    x=rows[0][0]
    if(password==x):
        print("1. Fix Appointment")
        print("2. Pay Bills")
        print("3. Geneartion of Inventory for Admit")
        print("4, Generation of Report")
        print("4. Quit")
        input_2=int(input("Enter the choice"))
        if(input_2==1):
            print("1.General")
            print("2. Ent")
            print("3. Eyes")
            input_3=int(input("Enter the choice"))
            if(input_3==1):
                name='GENERAL'
                cur.execute("Select * from Registration where Specialist=:param1",{'param1':name})
                rows3=cur.fetchall()
                doctorid=rows3[0][0]
                input_4=input("Enter the choice of shift")
                if(input_4=="Morning"):
                    appointment_fixation(username,name,appointment_no_morning,patient_count_morning,input_4,doctorid)
                elif (input_4=="Evening"):
                    appointment_fixation(username,name,appointment_no_evening,patient_count_evening,input_4,doctorid)
                        
                        
            if(input_3==2):
                name='ENT'
                cur.execute("Select *  from Registration where Specialist=:param1",{'param1':name})
                rows6=cur.fetchall()
                a=rows6[0][0]
                c=rows6[0][1]
                b=rows6[1][0]
                d=rows6[1][1]
                print("1.",c,"\t\t 2.",d)
                input_8=int(input("Enter Choice"))
                if(input_8 == 1):
                    input_10=input("Enter the shift:")
                    if(input_10=="Morning"):
                        appointment_fixation(username,name,appointment_no_morning1,patient_count_morning1,input_10,a)
                    elif(input_10=="Evening"):
                        appointment_fixation(username,name,appointment_no_evening1,patient_count_evening1,input_10,a)
                elif(input_8 == 2):
                    input_10=input("Enter the shift:")
                    if(input_10=="Morning"):
                        appointment_fixation(username,name,appointment_no_morning2,patient_count_morning2,input_10,b)
                    elif(input_10=="Evening"):
                        appointment_fixation(username,name,appointment_no_evening2,patient_count_evening2,input_10,b)



            if(input_3==3):
                    name='Eyes'
                    cur.execute("Select * from Registration where Specialist=:param1",{'param1':name})
                    rows3=cur.fetchall()
                    print(rows3)
                    doctorid=rows3[0][0]
                    print(doctorid)
                    input_4=input("Enter the choice of shift")
                    if(input_4=="Morning"):
                        appointment_fixation(username,name,appointment_no_morning3,patient_count_morning3,input_4,doctorid)
                    elif (input_4=="Evening"):
                        appointment_fixation(username,name,appointment_no_evening3,patient_count_evening3,input_4,doctorid)




        if(input_2==2):
            payment_gateway(username)


        if(input_2==3):
            inventory_setup(username)

def collect_sample(input_12):
    input_13=input("Enter Result of the test")
    cur.execute("Update Labtest SET  COLLECTSAMPLE='Yes' , RESULT=:param1 WHERE UserId=:param2" ,{'param1':input_13,'param2':input_12})
    #con.commit()

def report_generation(username):
    cur.execute("Select * from Registration where Userid=:param1",{'param1':username})
    rows5=cur.fetchall()
    a1=rows5[0][0]
    a2=rows5[0][1]
    a3=rows5[0][2]
    a4=rows5[0][3]
    a5=rows5[0][4]
    a6=rows5[0][5]
    a7=rows5[0][6]
    a8=rows5[0][7]
    a9=rows5[0][8]
    a10=rows5[0][9]
    a11=rows5[0][10]
    a12=rows5[0][11]
    a13=rows5[0][12]
    a14=rows5[0][13]
    a15=rows5[0][14]
    cur.execute("Select * from LABTEST WHERE USERID=:param1",{'param1':username})
    rows7=cur.fetchall()
    a16=rows7[0][1]
    a17=rows7[0][2]
    labtest1=LabTest(a1,a2,a3,a4,a5,a7,a11,a6,a8,a9,a10,a12,a13,a14,a15,a16,a17,report_no+1)
    cur.execute("UPDATE LABTEST SET ReportNummber  = :param1 WHERE UserID = :param2",{'param1':labtest1.reportno,'param2':username})

    
    #con.commit()
    labtest1.print_labtest()

def validation(username):
    cur.execute("Select * from Registration where Userid=:param1",{'param1':username})
    rows5=cur.fetchall()
    a1=rows5[0][0]
    a2=rows5[0][1]
    a3=rows5[0][2]
    a4=rows5[0][3]
    a5=rows5[0][4]
    a6=rows5[0][5]
    a7=rows5[0][6]
    a8=rows5[0][7]
    a9=rows5[0][8]
    a10=rows5[0][9]
    a11=rows5[0][10]
    a12=rows5[0][11]
    a13=rows5[0][12]
    a14=rows5[0][13]
    a15=rows5[0][14]
    cur.execute("Select * from LABTEST WHERE USERID=:param1",{'param1':username})
    rows7=cur.fetchall()
    a16=rows7[0][1]
    a17=rows7[0][2]
    a18=rows7[0][3]
    labtest1=LabTest(a1,a2,a3,a4,a5,a7,a11,a6,a8,a9,a10,a12,a13,a14,a15,a16,a17,a18)
    labtest1.print_labtest()
    



def laboratory_functionality():
    username=input("Enter the UserName :")
    password=input("Enter the password:")
    cur.execute("Select Password from Registration  where Userid=:param1",{'param1':username});
    rows=cur.fetchall()
    x=rows[0][0]
    if(password==x):
        print("1. Collect Sample")
        print("2. Report Generation")
        print("3. Validation")
        print("4. Quit")
        input_2=int(input("Enter the choice"))
        input_12=input("Enter Patient ID:")
        if(input_2==1):
            collect_sample(input_12);
        if(input_2==2):
            report_generation(input_12)
        if(input_2==3):
            validation(input_12)
    
                
            
                
                
                    
            
            
def inventory_setup(username):
    bedno=0
    wardno=1
    cur.execute("Select * from Registration where UserId=:param1",{'param1':username})
    rows5= cur.fetchall()
    a1=rows5[0][0]
    a2=rows5[0][1]
    a3=rows5[0][2]
    a4=rows5[0][3]
    a5=rows5[0][4]
    a6=rows5[0][5]
    a7=rows5[0][6]
    a8=rows5[0][7]
    a9=rows5[0][8]
    a10=rows5[0][9]
    a11=rows5[0][10]
    a12=rows5[0][11]
    a13=rows5[0][12]
    a14=rows5[0][13]
    a15=rows5[0][14]
    if(a15=="Yes"):
        if(wardno == no_of_wards):
            print("No wards are available")
                       
        elif (bedno==5):
            wardno=wardno+1

        else:
            bedno=bedno+1
            a1=Admit(a1,a2,a3,a4,a5,a7,a11,a6,a8,a9,a10,a12,a13,a14,a15,wardno,bedno)
            a1.print_inventory()
        
                
                

                
    
def appointment_fixation(username,name,appointment_no,patient_count,input_4,doctorid):
    cur.execute("Select * from Schedule where UserID=:param1 And Type=:param2" ,{'param1':doctorid,'param2':input_4})
    rows4=cur.fetchall()
    duration=rows4[0][4]
    duration=float(duration)-.25
    appointment_no=appointment_no+1
    if(duration==0.0):
        print("Appointments are full")
    else:
        cur.execute("Update Schedule SET Duration=:param1 WHERE UserID=:param2 AND Type=:param3" ,{'param1':duration,'param2':doctorid,'param3':input_4})
        #con.commit()
        cur.execute("Select * from Registration where UserId=:param1",{'param1':username})
        rows5=cur.fetchall()
        a1=rows5[0][0]
        print(a1)
        a2=rows5[0][1]
        a3=rows5[0][2]
        a4=rows5[0][3]
        a5=rows5[0][4]
        a6=rows5[0][5]
        a7=rows5[0][6]
        a8=rows5[0][7]
        a9=rows5[0][8]
        a10=rows5[0][9]
        a11=rows5[0][10]
        a12=rows5[0][11]
        a13=rows5[0][12]
        a14=rows5[0][13]
        a15=rows5[0][14]
        #def __init__(self,UserId,UserName,Password,Email,MobileNo,dob,age,gender,height,weight,designation,specialist,prescription,labtest,admit,type_1,AppnNo):
        app1=Appointment(a1,a2,a3,a4,a5,a7,a11,a6,a8,a9,a10,a12,a13,a14,a15,input_4,appointment_no)
        app1.print_appointment()
        patient_count=patient_count+1
        cur.execute("Update Schedule SET PatientCount=:param1 WHERE UserID=:param2 AND Type=:param3" ,{'param1':patient_count,'param2':doctorid,'param3':input_4})
        #con.commit()
            
    
    
def payment_gateway(username):
    cur.execute("Select * from Registration where UserId=:param1",{'param1':username})
    rows7=cur.fetchall()
    y=rows7[0][13]
    z=rows7[0][14]
    if((y=="Yes")and(z=="Yes")):
        input_11 = int(input("Enter the number of days:"))
        admitcharge=adm_charges*input_11
        pay=consultantfees+labtest+admitcharge
        print("The Amount That has to be paid is :",pay)
        input12=input("Press any key to pay")
        cardnumber=int(input("Enter Card Number:"))
        expiry_date=input("Enter Exipry date:")
        cvv=int(input("Enter Cvv Number:"))
        cardname=input("Enter Card Name")

    elif (y=="Yes"):
        pay=consultantfees+labtest
        print("The Amount That has to be paid is :",pay)
        input12=input("Press any key to pay")
        cardnumber=int(input("Enter Card Number:"))
        expiry_date=input("Enter Exipry date:")
        cvv=int(input("Enter Cvv Number:"))
        cardname=input("Enter Card Name")

    else:
        pay=consultantfees
        print("The Amount That has to be paid is :",pay)
        input12=input("Press any key to pay")
        cardnumber=int(input("Enter Card Number:"))
        expiry_date=input("Enter Exipry date:")
        cvv=int(input("Enter Cvv Number:"))
        cardname=input("Enter Card Name")
    
    

con=cx_Oracle.connect("PYTHONDB/Laksham1234@localhost/xe")
cur=con.cursor()


print ("\n\n ----------Welcome to the HeltCare Hospital-------------")
print("\n")
print("1. New User")
print("2. Existing User")
ch=int(input("Enter the choice"))
if(ch==1):
    personal_details()
    
if(ch == 2):
    print("Main Menu:")
    print("1. Doctor")
    print("2. Patient")
    print("3. Laboratorist")
    print("4. Quit")
    choice=int(input("Please Enter the Option"))
    if (choice ==1):
        doctor_functionality()
    if (choice == 2):
        patient_functionality()
    if (choice == 3):
        laboratory_functionality()
        
        

                    
                    
                





                            

            
                    

            

                        
                            
 
                        
                        
                     
                    
                    
                    
                    
                    
                    
                    
                    
                    
                

        
        
                
    

              
            

    
    

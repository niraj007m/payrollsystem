from tkinter import*
import random 
import time
import datetime
import string

payroll = Tk()
payroll.geometry("895x525+0+0")
payroll.title("PMS - Payroll Systems")
#payroll.configure(background='magenta')

def Exit():
	payroll.destroy()

def Reset():
	EmployeeName.set("")
	Address.set("")
	Reference.set("")
	EmployerName.set("")
	Email.set("")
	JobStatus.set("")
	City.set("")
	BasicSalary.set("")
	OverTime.set("")
	GrossPay.set("")
	NetPay.set("")
	Tax.set("")
	Pension.set("")
	StudentLoan.set("")
	NIPayment.set("")
	Deductions.set("")
	PostCode.set("")
	Gender.set("")
	Grade.set("")
	Department.set("")
	PayDate.set("")
	TaxPeriod.set("")
	NINumber.set("")
	NICode.set("")
	TaxablePay.set("") 
	PensionPay.set("")
	OtherPaymentDue.set("")
def PayRef():
	PayDate.set(time.strftime("%d/%m/%y"))
	#PayDate.set(time.strftime("%x"))

	Refpay = random.randint(20000, 709467)
	Refpaid = ("PR" + str(Refpay))
	Reference.set(Refpaid)

	NIpay = random.randint(4200, 9467)
	NIpaid = ("NI" + str(NIpay))
	NINumber.set(NIpaid)

def PayPeriod():
	i = datetime.datetime.now()
	TaxPeriod.set(i.month)

	NCode = random.randint(1200, 4467)
	Cod = ("NICode" + str(NCode))
	NICode.set(Cod)

def MonthlySalary():

	BS = float(BasicSalary.get())
	CW = float(City.get())
	OT = float(OverTime.get())
	#BS = float(BasicSalary.get()) if '.' in BasicSalary.get() else str(BasicSalary.get())
	#CW = float(City.get()) if '.' in City.get() else str(City.get())
	#OT = float(OverTime.get()) if '.' in OverTime.get() else str(OverTime.get())

	MTax = ((BS + CW + OT) * 0.5)
	TTax = "₹", str('%.2f'%(MTax))
	Tax.set(TTax)

	M_Pension = ((BS + CW + OT) * 0.026)
	MM_Pension = "₹", str('%.2f'%(M_Pension))
	Pension.set(MM_Pension)

	M_StudentLoan = ((BS + CW + OT) * 0.012)
	MM_StudentLoan = "₹", str('%.2f'%(M_StudentLoan))
	StudentLoan.set(MM_StudentLoan)

	M_NIPayment = ((BS + CW + OT) * 0.011)
	MM_NIPayment = "₹", str('%.2f'%(M_NIPayment))
	NIPayment.set(MM_NIPayment)

	Deduct = (MTax + M_Pension + M_StudentLoan + M_NIPayment)
	Deduct_Payment = "₹", str('%.2f' %(Deduct))
	Deductions.set(Deduct_Payment)

	Gross_Pay = "₹", str('%.2f' % (BS + CW + OT))
	GrossPay.set(Gross_Pay)

	NetPayAfter = (BS + CW + OT) - Deduct
	NetAfter = "₹", str('%.2f' %(NetPayAfter))
	NetPay.set(NetAfter)

	TaxablePay.set(TTax)
	PensionPay.set(MM_Pension)
	OtherPaymentDue.set("0")


EmployeeName = StringVar()
Address = StringVar()
Reference = StringVar()
EmployerName = StringVar()
Email = StringVar()
JobStatus = StringVar()
City = StringVar()
BasicSalary = StringVar()
OverTime = StringVar()
GrossPay = StringVar()
NetPay = StringVar()
Tax = StringVar()
Pension = StringVar()
StudentLoan = StringVar()
NIPayment = StringVar() 
Deductions = StringVar()
PostCode = StringVar()
Gender = StringVar()
Grade = StringVar()
Department = StringVar()
PayDate = StringVar()
TaxPeriod = StringVar() 
NINumber = StringVar()
NICode = StringVar()
TaxablePay = StringVar() 
PensionPay = StringVar() 
OtherPaymentDue = StringVar()

Tops=Frame(payroll, width=1350, height=50, bd=2, relief="raise")
Tops.pack(side=TOP)
LF=Frame(payroll, width=700, height=650, bd=2, relief="raise")
LF.pack(side=LEFT)
RF=Frame(payroll, width=600, height=650, bd=2, relief="raise")
RF.pack(side=RIGHT)

lblInfo = Label(Tops, font=('arial',50,'bold'),text="Payroll Systems", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0,column=0)


LeftInsideLF=Frame(LF, width=700, height=100, bd=3, relief="raise")
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame(LF, width=325, height=400, bd=3, relief="raise")
LeftInsideLFLF.pack(side=LEFT)
LeftInsideRFRF=Frame(LF, width=325, height=400, bd=3, relief="raise")
LeftInsideRFRF.pack(side=RIGHT)

RightInsideLF=Frame(RF, width=600, height=200, bd=3, relief="raise")
RightInsideLF.pack(side=TOP)
RightInsideLFLF=Frame(RF, width=300, height=400, bd=3, relief="raise")
RightInsideLFLF.pack(side=LEFT)
RightInsideRFRF=Frame(RF, width=300, height=400, bd=3, relief="raise")
RightInsideRFRF.pack(side=RIGHT)

lblEmployeeName = Label(LeftInsideLF, font=('arial',12,'bold'),text="Employee Name", fg="Steel Blue", bd=10, anchor='w')
lblEmployeeName.grid(row=0,column=0)
txtEmployeeName = Entry(LeftInsideLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=54, justify='left', textvariable=EmployeeName)
txtEmployeeName.grid(row=0,column=1)
lblAddress = Label(LeftInsideLF, font=('arial',12,'bold'),text="Address", fg="Steel Blue", bd=10, anchor='w')
lblAddress.grid(row=1,column=0)
txtAddress = Entry(LeftInsideLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=54, justify='left', textvariable=Address)
txtAddress.grid(row=1,column=1)

lblRefrence = Label(LeftInsideLF, font=('arial',12,'bold'),text="Reference", fg="Steel Blue", bd=10, anchor='w')
lblRefrence.grid(row=2,column=0)
txtRefrence = Entry(LeftInsideLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=54, justify='left', textvariable=Reference)
txtRefrence.grid(row=2,column=1)
lblEmployerName = Label(LeftInsideLF, font=('arial',12,'bold'),text="Employer Name", fg="Steel Blue", bd=10, anchor='w')
lblEmployerName.grid(row=3,column=0)
txtEmployerName = Entry(LeftInsideLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=54, justify='left', textvariable=EmployerName)
txtEmployerName.grid(row=3,column=1)

lblEmail = Label(LeftInsideLF, font=('arial',12,'bold'),text="Email", fg="Steel Blue", bd=10, anchor='w')
lblEmail.grid(row=4,column=0)
txtEmail = Entry(LeftInsideLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=54, justify='left', textvariable=Email)
txtEmail.grid(row=4,column=1)
lblJobStatus = Label(LeftInsideLF, font=('arial',12,'bold'),text="Job Status", fg="Steel Blue", bd=10, anchor='w')
lblJobStatus.grid(row=5,column=0)
txtJobStatus = Entry(LeftInsideLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=54, justify='left', textvariable=JobStatus)
txtJobStatus.grid(row=5,column=1)

lblCity = Label(LeftInsideLFLF, font=('arial',12,'bold'),text="City Weighting", fg="Steel Blue", bd=10, anchor='w')
lblCity.grid(row=0,column=0)
txtCity = Entry(LeftInsideLFLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=18, justify='left', textvariable=City)
txtCity.grid(row=0,column=1)

lblBasicSalary = Label(LeftInsideLFLF, font=('arial',12,'bold'),text="Basic Salary", fg="Steel Blue", bd=10, anchor='w')
lblBasicSalary.grid(row=1,column=0)
txtBasicSalary = Entry(LeftInsideLFLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=18, justify='left', textvariable=BasicSalary)
txtBasicSalary.grid(row=1,column=1)

lblOverTime = Label(LeftInsideLFLF, font=('arial',12,'bold'),text="Over Time", fg="Steel Blue", bd=10, anchor='w')
lblOverTime.grid(row=2,column=0)
txtOverTime = Entry(LeftInsideLFLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=18, justify='left', textvariable=OverTime)
txtOverTime.grid(row=2,column=1)

lblGrossPay = Label(LeftInsideLFLF, font=('arial',12,'bold'),text="GrossPay", fg="Steel Blue", bd=10, anchor='w')
lblGrossPay.grid(row=3,column=0)
txtGrossPay = Entry(LeftInsideLFLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=18, justify='left', textvariable=GrossPay)
txtGrossPay.grid(row=3,column=1)

lblNetPay = Label(LeftInsideLFLF, font=('arial',12,'bold'),text="Net Pay", fg="Steel Blue", bd=10, anchor='w')
lblNetPay.grid(row=4,column=0)
txtNetPay = Entry(LeftInsideLFLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=18, justify='left', textvariable=NetPay)
txtNetPay.grid(row=4,column=1)


lblTax = Label(LeftInsideRFRF, font=('arial',12,'bold'),text="Tax", fg="Steel Blue", bd=10, anchor='w')
lblTax.grid(row=0,column=0)
txtTax = Entry(LeftInsideRFRF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=18, justify='left', textvariable=Tax)
txtTax.grid(row=0,column=1)

lblPension = Label(LeftInsideRFRF, font=('arial',12,'bold'),text="Pension", fg="Steel Blue", bd=10, anchor='w')
lblPension.grid(row=1,column=0)
txtPension = Entry(LeftInsideRFRF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=18, justify='left', textvariable=Pension)
txtPension.grid(row=1,column=1)

lblStudentLoan = Label(LeftInsideRFRF, font=('arial',12,'bold'),text="Student Loan", fg="Steel Blue", bd=10, anchor='w')
lblStudentLoan.grid(row=2,column=0)
txtStudentLoan = Entry(LeftInsideRFRF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=18, justify='left', textvariable=StudentLoan)
txtStudentLoan.grid(row=2,column=1)

lblNIPayment = Label(LeftInsideRFRF, font=('arial',12,'bold'),text="NI Payment", fg="Steel Blue", bd=10, anchor='w')
lblNIPayment.grid(row=3,column=0)
txtNIPayment = Entry(LeftInsideRFRF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=18, justify='left', textvariable=NIPayment)
txtNIPayment.grid(row=3,column=1)

lblDeductions = Label(LeftInsideRFRF, font=('arial',12,'bold'),text="Deductions", fg="Steel Blue", bd=10, anchor='w')
lblDeductions.grid(row=4,column=0)
txtDeductions = Entry(LeftInsideRFRF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=18, justify='left', textvariable=Deductions)
txtDeductions.grid(row=4,column=1)



lblPostCode = Label(RightInsideLF, font=('arial',12,'bold'),text="Post Code", fg="Steel Blue", bd=10, anchor='w')
lblPostCode.grid(row=0,column=0)
txtPostCode = Entry(RightInsideLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=54, justify='left', textvariable=PostCode)
txtPostCode.grid(row=0,column=1)
lblGender = Label(RightInsideLF, font=('arial',12,'bold'),text="Gender", fg="Steel Blue", bd=10, anchor='w')
lblGender.grid(row=1,column=0)
txtGender = Entry(RightInsideLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=54, justify='left', textvariable=Gender)
txtGender.grid(row=1,column=1) 

lblGrade = Label(RightInsideLF, font=('arial',12,'bold'),text="Grade", fg="Steel Blue", bd=10, anchor='w')
lblGrade.grid(row=2,column=0)
txtGrade = Entry(RightInsideLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=54, justify='left', textvariable=Grade)
txtGrade.grid(row=2,column=1)
lblDepartment = Label(RightInsideLF, font=('arial',12,'bold'),text="Department", fg="Steel Blue", bd=10, anchor='w')
lblDepartment.grid(row=3,column=0)
txtDepartment = Entry(RightInsideLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=54, justify='left', textvariable=Department)
txtDepartment.grid(row=3,column=1) 


lblPayDate = Label(RightInsideLFLF, font=('arial',12,'bold'),text="Pay Date - d/m/y", fg="Steel Blue", bd=10, anchor='w')
lblPayDate.grid(row=0,column=0)
txtPayDate = Entry(RightInsideLFLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=18, justify='left', textvariable=PayDate)
txtPayDate.grid(row=0,column=1)

lblTaxPeriod = Label(RightInsideLFLF, font=('arial',12,'bold'),text="Tax Period", fg="Steel Blue", bd=10, anchor='w')
lblTaxPeriod.grid(row=1,column=0)
txtTaxPeriod = Entry(RightInsideLFLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=18, justify='left', textvariable=TaxPeriod)
txtTaxPeriod.grid(row=1,column=1)

lblNINumber = Label(RightInsideLFLF, font=('arial',12,'bold'),text="NI Number", fg="Steel Blue", bd=10, anchor='w')
lblNINumber.grid(row=2,column=0)
txtNINumber = Entry(RightInsideLFLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=18, justify='left', textvariable=NINumber)
txtNINumber.grid(row=2,column=1)

lblNICode = Label(RightInsideLFLF, font=('arial',12,'bold'),text="NI Code", fg="Steel Blue", bd=10, anchor='w')
lblNICode.grid(row=3,column=0)
txtNICode = Entry(RightInsideLFLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=18, justify='left', textvariable=NICode)
txtNICode.grid(row=3,column=1)

lblTaxablePay = Label(RightInsideLFLF, font=('arial',12,'bold'),text="Taxable Pay", fg="Steel Blue", bd=10, anchor='w')
lblTaxablePay.grid(row=4,column=0)
txtTaxablePay = Entry(RightInsideLFLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=18, justify='left', textvariable=TaxablePay)
txtTaxablePay.grid(row=4,column=1)

lblPensionPay = Label(RightInsideLFLF, font=('arial',12,'bold'),text="Pension Pay", fg="Steel Blue", bd=10, anchor='w')
lblPensionPay.grid(row=5,column=0)
txtPensionPay = Entry(RightInsideLFLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=18, justify='left', textvariable=PensionPay)
txtPensionPay.grid(row=5,column=1)

lblOtherPaymentDue = Label(RightInsideLFLF, font=('arial',12,'bold'),text="Other Payment Due", fg="Steel Blue", bd=10, anchor='w')
lblOtherPaymentDue.grid(row=6,column=0)
txtOtherPaymentDue = Entry(RightInsideLFLF, font=('arial',12,'bold'), bg="powder blue", bd=1, width=18, justify='left', textvariable=OtherPaymentDue)
txtOtherPaymentDue.grid(row=6,column=1)

btnWagePayment=Button(RightInsideRFRF,padx=8, bd=8, fg="black", font=('arial',16,'bold'), width=18, text="Wage Payment", bg="powder blue", command=MonthlySalary).grid(row=1,column=0 )
btnReset=Button(RightInsideRFRF,padx=8, bd=8, fg="black", font=('arial',16,'bold'), width=18, text="Reset System", bg="powder blue", command=Reset).grid(row=2,column=0 )
btnPayRef=Button(RightInsideRFRF,padx=8, bd=8, fg="black", font=('arial',16,'bold'), width=18, text="Pay Reference", bg="powder blue", command=PayRef).grid(row=3,column=0 )
btnPayCode=Button(RightInsideRFRF,padx=8, bd=8, fg="black", font=('arial',16,'bold'), width=18, text="Pay Code", bg="powder blue", command=PayPeriod).grid(row=4,column=0 )
btnExit=Button(RightInsideRFRF,padx=8, bd=8, fg="black", font=('arial',16,'bold'), width=18, text="Exit", bg="powder blue", command=Exit).grid(row=5,column=0 )


payroll.mainloop()


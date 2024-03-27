from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, UserRegistrationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Register
from .models import Trans
from .models import Employee
from .models import Truck
from .models import Worker
from .models import Billing
import io
#from rest_framework.decorators import api_view, renderer_classes
#from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.hashers import make_password
import pdfkit
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors
# from weasyprint import HTML
from .models import Invoice
from datetime import datetime






# Create your views here.
@login_required
def Vendor(request):
    if request.method == "POST":
        cname       =   request.POST.get('companyname')
        address     =   request.POST.get('address')
        gst         =   request.POST.get('gst')
        contactno   =   request.POST.get('contact_no')
        contactperson   = request.POST.get('contact_person')
        transport   = request.POST.get('transport')

        
        vendor  = Register()
        vendor.cname=cname
        vendor.address=address
        vendor.gst=gst
        vendor.contactno=contactno
        vendor.contactperson=contactperson
        vendor.transId_id=transport
        vendor.save()
        return redirect('/vendorlist')
        
    query =     Trans.objects.all()
    data =  {
        'query':query
    }
    return render(request, 'Vendor.html', data)


@login_required
def vendorlist(request):
    query   =   Register.objects.all()  
    data = {
        'query':query,
    }
    return render(request,'vendorlist.html',data)


@login_required
def vendoreditlist(request, id):
        query = ''
        if request.method == 'POST':
            cname       =   request.POST.get('companyname')
            address     =   request.POST.get('address')
            gst         =   request.POST.get('gst')
            contactno   =  request.POST.get('contact_no')
            contactperson   =  request.POST.get('contact_person')
            
                        
            Register.objects.filter(id=id).update(cname=cname, address=address, gst=gst, contactno=contactno, contactperson=contactperson)
            return redirect("vendorlist")
        if id:
            query=Register.objects.filter(id=id).first()
            truck  = Trans.objects.all()
            
            data={
                'vendordata' : query,
                'truck' : truck
                }
            return render(request, 'vendoreditlist.html',data)

def detelevendor(request, id):
    Register.objects.filter(id=id).delete()
    return redirect("vendorlist")


@login_required
def transport(request):
    if request.method == "POST":
        name        =  request.POST.get('username')
        password    =  request.POST.get('password')
        cname       =   request.POST.get('companyname')
        address     =   request.POST.get('address')
        gst         =   request.POST.get('gst')
        contactno   =   request.POST.get('contact_no')
        contactperson   =   request.POST.get('contact_person')
        hashed_password = make_password(password, hasher='pbkdf2_sha256')
        image = request.FILES["image"]
        
        transport   =  Trans()
        transport.name=name
        transport.password=password
        transport.cname=cname
        transport.address=address
        transport.gst=gst
        transport.contactno=contactno
        transport.contactperson=contactperson
        transport.image = image
        transport.save()
        
        return redirect('/transportlist')
    return render(request, 'transport.html', )

@login_required
def transportlist(request):
    query   =   Trans.objects.all()  
    #print(query)
    return render(request,'transportlist.html',{'query':query})

@login_required
def transporteditlist(request, id):
        query = ''
        if request.method == 'POST':
            name        =  request.POST.get('Username')
            password    =  request.POST.get('Password')
            cname       =   request.POST.get('companyname')
            address     =   request.POST.get('address')
            gst         =   request.POST.get('gst')
            contactno   =  request.POST.get('contact_no')
            contactperson   =  request.POST.get('contact_person')
            
            Trans.objects.filter(id=id).update(name=name,password=password,cname=cname, address=address, gst=gst, contactno=contactno, contactperson=contactperson)
            return redirect("transportlist")
        if id:
            query=Trans.objects.filter(id=id).first()
            data={
                'transportdata' : query
                }
            return render(request, 'transporteditlist.html',data)
def deteletransport(request, id):
    Trans.objects.filter(id=id).delete()
    return redirect("transportlist")





@login_required
def index(request):
    return render(request, 'index.html', {})

@login_required
# def signup(request):
#     form = UserRegistrationForm()
#     if request.method == "POST":
#         name        =   request.POST.get('Username')
#         password    =   request.POST.get('Password')
#         email       =   request.POST.get('Email')
#         phone       =   request.POST.get('Phone')
#         new_user = User(username=name, email=email, password=hashed_password, is_staff='1', is_superuser='1')
#         hashed_password = make_password(password, hasher='pbkdf2_sha256')
        
#         employee    =   Employee()
#         employee.name=name
#         employee.password=password
#         employee.email=email
#         employee.phone=phone
#         User.userid=new_user
#         employee.save()
        
        
#         try:
#             new_user.save()
#         except:
#             return HttpResponse("Something Went Wrong.")
#           token = Token.objects.create(user=new_user)
#         return  redirect('login')
#     return render(request, 'signup.html', {'form':form})
def signup(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        name = request.POST.get('Username')
        password = request.POST.get('Password')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        
        # Hash the password
        hashed_password = make_password(password, hasher='pbkdf2_sha256')
        
        # Create a new user
        new_user = User(username=name, email=email, password=hashed_password, is_staff='1', is_superuser='1')
        print(new_user)
        # Save the user
        try:
            new_user.save()
        except:
            return HttpResponse("Something Went Wrong.")
        
        # Generate a token for the user
        token = Token.objects.create(user=new_user)
        print([token])
        # Create a response with the token
        response_data = {
            'token': token.key,
            'user_id': new_user.id,
            'username': new_user.username,
            # Add other user details as needed
        }
        print(response_data)
        #return Response(response_data)
        return redirect('login')
    
    return render(request, 'signup.html', {'form': form})

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def verify_token(request):
    if request.user.is_authenticated:
        # User is authenticated, token is valid
        return Response({'message': 'Token is valid'})
    else:
        # Token is invalid or expired
        return Response({'error': 'Token is invalid'}, status=401)

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user.id)
        if user is not None:
            login(request, user)
            session_id = request.session.session_key
            print("Session ID:", session_id)

            # Check if token exists for the user
            token = Token.objects.filter(user=user).first()
            if not token:
                # If token doesn't exist, create one
                token = Token.objects.create(user=user)
            print(token)
            return redirect('transport')
        else:
            return HttpResponse("Invalid credentials.")
    else:
        form = UserForm()
        return render(request, 'login.html', {'form': form})
    
    
def signout(request):
    logout(request)
    return  redirect('/')

@login_required
def Operator(request):
    if request.method == "POST":
        dname       =   request.POST.get('Dname')
        dcontact    =   request.POST.get('Dcontactno')
        truckno     =   request.POST.get('Truckno')
        oname       =   request.POST.get('Oname')
        ocontact    =   request.POST.get('Ocontactno')
        Ttype       =    request.POST.get('Ttype')
        transport   = request.POST.get('transport')


        truck       =   Truck()
        truck.dname=dname
        truck.dcontact=dcontact
        truck.truckno=truckno
        truck.oname=oname
        truck.ocontact=ocontact
        truck.Ttype=Ttype
        truck.transId_id=transport
        truck.save()
        return redirect('/trucklist')
        
    query       = Trans.objects.all()
    data  = {
        'query':query
    }

    return render(request, 'truck.html',data)

@login_required
def Trucklist(request):
    query   =   Truck.objects.all()  
    return render(request,'trucklist.html',{'query':query})


@login_required
def Truckeditlist(request, id):
        query = ''
        if request.method == 'POST':
            dname       =  request.POST.get('Dname')
            dcontact    =  request.POST.get('Dcontactno')
            truckno     =  request.POST.get('Truckno')
            oname       =  request.POST.get('Oname')
            ocontact    =  request.POST.get('Ocontactno')
            Ttype       =  request.POST.get('Ttype')
            
            Truck.objects.filter(id=id).update(dname=dname,dcontact=dcontact,truckno=truckno, oname=oname, ocontact=ocontact, Ttype=Ttype)
            return redirect("trucklist")
        if id:
            query=Truck.objects.filter(id=id).first()
            truck  = Trans.objects.all()
            
            data={
                'Truckdata' : query,
                'truck':truck
                
                }
            return render(request, 'truckeditlist.html',data)
        
        
def deletetruck(request, id):
    Truck.objects.filter(id=id).delete()
    return redirect("trucklist")


@login_required
def labour(request):
    if request.method == "POST":
        lname      = request.POST.get('Lname')
        address     = request.POST.get('address')
        contactno   = request.POST.get('contact_no')
        transport   = request.POST.get('transport')

        print(lname)
        
        worker      = Worker()
        worker.lname=lname
        worker.address=address
        worker.contactno=contactno
        worker.transId_id=transport
        worker.save()
        return redirect('/labourlist')
    query       = Trans.objects.all()
    data  = {
        'query':query
    }
    return render(request, 'labour.html', data)
    
    
@login_required
def labourlist(request):
    query   =   Worker.objects.all()  
    return render(request,'labourlist.html',{'query':query})


@login_required
def laboureditlist(request, id):
        if request.method == 'POST':
            lname       =  request.POST.get('Lname')
            address    =  request.POST.get('address')
            contactno  =  request.POST.get('contact_no')
                        
            Worker.objects.filter(id=id).update(lname=lname,address=address,contactno=contactno)
            return redirect("labourlist")
        if id:
            query=Worker.objects.filter(id=id).first()
            truck  = Trans.objects.all()
            data={
                'labourdata' : query,
                'truck' : truck
                }
            return render(request, 'laboureditlist.html',data)
        
        
def deletelabour(request, id):
    Worker.objects.filter(id=id).delete()
    return redirect("labourlist")

def invoice(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        gst = request.POST.get('gst')
        inv_date = request.POST.get('inv_date')
        from1 = request.POST.get('from')
        to = request.POST.get('to')
        Lrno = request.POST.getlist('lr_no[]')
        trucknoList = request.POST.getlist('Truck[]')
        descriptions_list = request.POST.getlist('discriptions[]')
        weight_list = request.POST.getlist('weight[]')
        rate_list = request.POST.getlist('rate[]')
        amount_list = request.POST.getlist('amount[]')
        cDate = request.POST.getlist('c_date[]')
        cinvno = request.POST.getlist('c_inv_no[]')
        
       
        for lrno in Lrno:
            print(lrno)
      
        exit

        # Create a comma-separated string for each list
        descriptions = ",".join(descriptions_list)
        weights = ",".join(weight_list)
        rates = ",".join(rate_list)
        amounts = ",".join(amount_list)
        truckno = ",".join(trucknoList) if trucknoList else ''
        cDate = ",".join(cDate) if cDate else ''
        cinvno = ",".join(cinvno) if cinvno else ''
        lrno = ",".join(Lrno) if Lrno else ''
        inv_date = datetime.strptime(request.POST.get('inv_date'), '%Y-%m-%d').date()
        invMonth = inv_date.month
        fyYear = inv_date.year
        FyData = ''
        if(invMonth >= 4):
            FyData = f'{fyYear}-{fyYear+1}'
        else :
            FyData = f'{fyYear-1}-{fyYear}'
        lastInvoice = Billing.objects.filter(fy=FyData).last()
        preInv = 0;
        if(lastInvoice is not None):
            preInv = int(lastInvoice.inv_no)
        preInv += 1
        
        # print(descriptions)
        # exit()

        # Create a new Billing object and save it
        billing = Billing()
        billing.name = name
        billing.address = address
        billing.gst = gst
        billing.inv_date = inv_date
        billing.From = from1
        billing.truck = truckno
        billing.c_date = cDate
        billing.Lr_no =lrno
        billing.c_inv_no=cinvno
        billing.To = to
        billing.truck_id = truckno
        billing.Dsicriptions = descriptions
        billing.Qty_weight = weights
        billing.Rate = rates
        billing.Amount = amounts
        billing.fy = FyData
        billing.inv_no = preInv
        billing.save()
        
        return redirect('/invoicelist')
    
    query       = Truck.objects.all()
    data={
        'query' : query
    }
    return render(request, 'invoice.html', data)

def invoicelist(request):
    query   =   Billing.objects.all()
    return render(request,'invoicelist.html',{'query':query})

def invoiceeditlist(request, id):
    if request.method == 'POST':
        name          =  request.POST.get('name')
        address       =  request.POST.get('address')
        gst           =  request.POST.get('gst')
        inv_date = request.POST.get('inv_date')
        from1         =  request.POST.get('from')
        to            =  request.POST.get('to')
        Lrno          =  request.POST.get('Lr_no')
        truckno       =  request.POST.get('Truck')
        descriptions_list = request.POST.getlist('discriptions')
        weight_list = request.POST.getlist('weight')
        rate_list = request.POST.getlist('rate')
        amount_list = request.POST.getlist('amount')
             
        # lastInvoice = Billing.objects.filter(f)

        # Create a comma-separated string for each list
        descriptions = ",".join(descriptions_list)
        weights = ",".join(weight_list)
        rates = ",".join(rate_list)
        amounts = ",".join(amount_list)

        
        Billing.objects.filter(id=id).update(name=name,address=address,gst=gst,inv_date=inv_date,From=from1,To=to,Lr_no=Lrno,truck_id=truckno,Dsicriptions=descriptions,Qty_weight=weights,Rate=rates,Amount=amounts)
        return redirect("invoicelist")
    if id:
        query=Billing.objects.filter(id=id).first()
    if query:
        qty_weight_str = query.Qty_weight  # Assuming Qty_weight contains a comma-separated string
        Dsicriptions_str = query.Dsicriptions
        Rate_str = query.Rate
        Amount_str = query.Amount

        # Split the comma-separated string into individual values
        qty_weight_values = [value.strip() for value in qty_weight_str.split(',')]
        Dsicriptions_values = [value.strip() for value in Dsicriptions_str.split(',')]
        Rate_values = [value.strip() for value in Rate_str.split(',')]
        Amount_values = [value.strip() for value in Amount_str.split(',')]
            

        # Assuming you want to store the values in separate variables
        qty_weight1 = qty_weight_values[0] if qty_weight_values else None  # First value or None if empty
        qty_weight2 = qty_weight_values[1] if len(qty_weight_values) > 1 else None  # Second value or None if empty
        Dsicriptions1 = Dsicriptions_values[0] if Dsicriptions_values else None
        Dsicriptions2 = Dsicriptions_values[1] if len(Dsicriptions_values) > 1 else None
        Rate_values1 = Rate_values[0] if Rate_values else None
        Rate_values2 = Rate_values[1] if len(Rate_values) > 1 else None
        Amount_values1 = Amount_values[0] if Amount_values else None
        Amount_values2 = Amount_values[1] if len(Amount_values) > 1 else None
        truck       = Truck.objects.all()
        # Repeat as needed for additional values
        data={
            'invoicedata' : query,
            'qty_weight1' : qty_weight1,
            'qty_weight2' : qty_weight2,
            'Dsicriptions1' : Dsicriptions1,
            'Dsicriptions2' : Dsicriptions2,
            'Rate_values1' : Rate_values1,
            'Rate_values2' : Rate_values2,
            'Amount_values1' : Amount_values1,
            'Amount_values2' : Amount_values2,
            'truck' : truck
            }
        return render(request, 'invoiceeditlist.html',data)
        
        
def deleteinvoice(request, id):
    Billing.objects.filter(id=id).delete()
    return redirect("invoicelist")

def generate_pdf(request, id):
    if request.method == 'GET':
        # Fetch data from the database
        query = Billing.objects.filter(id=id).first()
        if query:
            width, height = A4
            styles = getSampleStyleSheet()
            styleN = styles["BodyText"]
            styleN.alignment = TA_LEFT
            styleBH = styles["Normal"]
            styleBH.alignment = TA_CENTER
            
            def coord(x, y, unit=1):
                x, y = x * unit, height -  y * unit
                return x, y
            
            # Headers
            srNoH = Paragraph('''<b>S.N</b>''', styleBH)
            DateClmnH = Paragraph('''<b>DATE</b>''', styleBH)
            lrNoH = Paragraph('''<b>L.R No</b>''', styleBH)
            truckNoH = Paragraph('''<b>Truck No</b>''', styleBH)
            descH = Paragraph('''<b>Descriptions Of Goods</b>''', styleBH)
            weightH = Paragraph('''<b>Qty Weight</b>''', styleBH)
            rateH = Paragraph('''<b>Rate</b>''', styleBH)
            amountH = Paragraph('''<b>Amount Rs</b>''', styleBH)
            
            data= [[srNoH, DateClmnH, lrNoH, truckNoH, descH, weightH, rateH, amountH]]
            
            # Create a PDF buffer
            buffer = io.BytesIO()

            # Define table data
            dateD = Paragraph(query.created_date.strftime("%Y-%m-%d") if query.created_date else '', styleN)
            lrNoD = Paragraph(str(query.Lr_no), styleN)
            truckD=Paragraph(query.truck.truckno,styleN)
            descriptionD = query.Dsicriptions.split(',')
            weightD = query.Qty_weight.split(',')
            rateD = query.Rate.split(',')
            amountD = query.Amount.split(',')
            zipped = zip(descriptionD, weightD, rateD, amountD)
            for desc, weight1, rate1, amount1 in zipped:
                descHP = Paragraph(desc, styleN)
                weightHP = Paragraph(weight1, styleN)
                rateHP = Paragraph(rate1, styleN)
                amountHP = Paragraph(amount1, styleN)
                #counterVal = forloop.counter
                rowData = ['1', dateD, lrNoD, truckD, descHP, weightHP, rateHP, amountHP]
                data.append(rowData)

            # Create table with calculated column widths
            table = Table(data, colWidths=[1.05*cm,2.45*cm, 1.5*cm,2.05*cm,4.05*cm,2.05*cm,2.05*cm,3.05*cm])
            table.setStyle(TableStyle([
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ]))
            
            pdf = canvas.Canvas("a.pdf", pagesize=A4)
            table.wrapOn(pdf, width, height)
            table.drawOn(pdf, *coord(1.8, 9.6, cm))
            pdf.save()

            # Add style to table
            # style = TableStyle([
            #     ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            #     ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            #     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            #     ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            #     ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            #     ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            #     ('GRID', (0, 0), (-1, -1), 1, colors.black),
            #     ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertical alignment
            #     ('WORDWRAP', (0, 1), (-1, -1), 1),  # Enable word wrap for values starting from the second row
            # ])
            # table.setStyle(style)

            # Add table to PDF document
            # elements.append(table)

            # # Build PDF
            # doc.build(elements)

            # # Get the value of the BytesIO buffer
            # pdf = buffer.getvalue()
            # buffer.close()

            # Create an HTTP response with the PDF as content
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="invoice_{id}.pdf"'
            response.write('a.pdf')

            return response

    # Handle other methods or invalid requests
    return HttpResponse("Invalid request")


def billhtml(request, id):
    invoice = Billing.objects.get(id=id)
    Truck    =   invoice.truck.split(',') if invoice.truck else []
    date    =   invoice.c_date.split(',') if invoice.c_date else []
    cinv_no  = invoice.c_inv_no.split(',') if invoice.c_inv_no else []
    lr_no       =   invoice.Lr_no.split(',') if invoice.Lr_no else []
    description  = invoice.Dsicriptions.split(',') if invoice.Dsicriptions else []
    qtyWeight = invoice.Qty_weight.split(',') if invoice.Qty_weight else []
    invRate = invoice.Rate.split(',') if invoice.Rate else []
    amount = invoice.Amount.split(',') if invoice.Amount else []
    data = zip(cinv_no,date,Truck,lr_no,description, qtyWeight, invRate, amount)

    context = {
        'invoice': invoice,
        'data' : data
    }
    return render(request, 'billformate.html', context)


def billformate(request, id):
    context = {}  # Define context variable outside the if block
    
    # if request.method == 'POST':
    invoice = Billing.objects.get(id=id)
    context = {
        'invoice': invoice
    }
    
    
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    htmlContent = f'http://127.0.0.1:8000/billhtml/{id}/'
    pdfkit.from_url(htmlContent, "generatedMyPdf.pdf", configuration=config)
        
    return render(request, 'billformate.html', context)


    
    # with open("generatedMyPdf.pdf", "rb") as pdf_file:
    #     response = HttpResponse(pdf_file.read(), content_type='application/pdf')
    #     response['Content-Disposition'] = 'attachment; filename="generatedMyPdf.pdf"'
    #     return response

from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from registration.supabase_client import supabase
from django.shortcuts import render, redirect

def registration_portal(request):
    """
    Render the main registration portal page.
    """
    return render(request, 'registration_portal.html')

@csrf_exempt
def register_laborer(request):
    if request.method == 'POST':
        try:
            # Collect form data
            name = request.POST.get('name')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            contact = request.POST.get('aadhaar')
            aadhaar = request.POST.get('aadhaar')
            education = request.POST.get('education')
            skill = request.POST.get('skill')
            current_location = request.POST.get('current_location')
            language = request.POST.get('language')

            if not (name and skill and current_location):
                return render(request, 'registration_portal.html', {
                    "error": "All fields are required."
                })

            # Insert into Supabase table
            response = supabase.from_('laborer').insert([{
                'name': name,
                'age': age,
                'gender': gender,
                'contact': contact,
                'aadhaar': aadhaar,
                'education': education,
                'skill': skill,
                'current_location': current_location,
                'language': language
            }]).execute()

            if response.get('status_code') == 201:
                return render(request, 'success.html', {"message": "Laborer registered successfully!"})
            else:
                error_message = response.get("data", {}).get("error", "An unexpected error occurred.")
                return render(request, 'error.html', {"error": error_message})

        except Exception as e:
            return render(request, 'error.html', {"error": f"An error occurred: {str(e)}"})
    else:
        return HttpResponseNotAllowed(['POST'], "Only POST requests are allowed.")

@csrf_exempt
def register_contractor(request):
    """
    Handle contractor registration via an HTML form.
    """
    if request.method == 'POST':
        try:
            # Get form data from request.POST
            company_name = request.POST.get('company_name')
            buisness_type = request.POST.get('buisness_type')
            contact_details = request.POST.get('contact_details')
            pan=request.POST.get('pan')
            job_posting=request.POST.get('job_posting')
            operational_location=request.POST.get('operational_location')

            if not (company_name and buisness_type and contact_details):

                return render(request, 'registration_portal.html', {
                    "error": "All fields are required."
                })

            # Insert into Supabase table
            response = supabase.from_('contractor').insert([{
                "company_name": company_name,
                "buisness_type": buisness_type,
                "contact_details": contact_details,
                "pan":pan,
                "job_posting":job_posting,
                "operational_location":operational_location,

            }]).execute()

            if response.get('status_code') == 201:
                return render(request, 'success.html', {"message": "Laborer registered successfully!"})
            else:
                error_message = response.get("data", {}).get("error", "An unexpected error occurred.")
                return render(request, 'error.html', {"error": error_message})
        except Exception as e:
            return render(request, 'error.html', {"error": f"An error occurred: {str(e)}"})
    else:
        return HttpResponseNotAllowed(['POST'], "Only POST requests are allowed.")


from django.shortcuts import render, redirect
from .forms import EmployeeForm


def employee_registration(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page
    else:
        form = EmployeeForm()

    
    return render(request, 'employee_form.html', {'form': form})

    

from django.shortcuts import render

def success(request):
    return render(request, 'success.html')
    

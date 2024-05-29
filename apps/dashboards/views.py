from django.views.generic import TemplateView
from web_project import TemplateLayout
from django.views.decorators.csrf import csrf_exempt
import os
from django.http import HttpResponse
import csv
import pandas as pd
from django.shortcuts import render
from django.utils.decorators import method_decorator
"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to dashboards/urls.py file for more pages.
"""


class DashboardsView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        print("called=========================")
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        print("POST==")
        result = pd.read_csv(self.request.FILES['file'])
        context.update({'data':result})
        print(context,"ll")
        filee= self.request.FILES['file'].read()
        print(result,"kkkkkkkkkkkkkk")
        print(filee)
        # data={'data':result}
        # Open the CSV file for reading
        data = handle_uploaded_file(self.request.FILES['file'],str(self.request.FILES['file']))
        print(data,"llllllllllllllllll")
        context.update({'data':data})
        
        # Your code here
        # Here request.POST is the same as self.request.POST
        # You can also access all possible self variables
        # like changing the template name for instance
        # bar = self.request.POST.get('foo', None)
        # file = self.request.POST.FILES['file']
        # if bar: self.template_name = 'path-to-new-template.html'
        # previous_foo = context['foo']
        # context['new_variable'] = 'new_variable' + ' updated'
        return self.render_to_response(context)

class DashboardsView1(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        print("called=========================")
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context
    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        print("----------POST----------------")
        # Your code here
        # Here request.POST is the same as self.request.POST
        # You can also access all possible self variables
        # like changing the template name for instance
        # bar = self.request.POST.get('foo', None)
        # file = self.request.POST.FILES['file']
        result = pd.read_csv(self.request.FILES['file'])

        print(result,"kkkkkkkkkkkkkk")
        # if bar: self.template_name = 'path-to-new-template.html'
        # previous_foo = context['foo']
        # context['new_variable'] = 'new_variable' + ' updated'
        return self.render_to_response(context)

def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + filename, 'r+') as destination:
        csv_reader = csv.reader(destination)
        for lines in csv_reader:
            print(lines)
        print("--------------------------------------------------")
        return lines[0].split(',')
        data_list = []
        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Append each row (as a dictionary) to the list
            data_list.append(row)
            # for chunk in file.chunks():
            #     destination.write(chunk)
        return data_list

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        # handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        result = pd.read_csv(request.FILES['file'])

        print(result)
        context = {'data': result,'layout_path':'layout/layout_vertical.html'}
        return render(request,"dashboard_analytics.html",{'layout_path':'layout/layout_vertical.html'})
        # return HttpResponse("Successful")

    return HttpResponse("Failed")


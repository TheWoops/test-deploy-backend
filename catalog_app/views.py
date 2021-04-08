from django.shortcuts import render
from django.views import generic

# Create your views here.
from catalog_app.models import Customer, System

# Used for POST requests
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from catalog_app.forms import UpdateCustomerForm
from django.contrib.auth.decorators import login_required, permission_required

# CRUD Operations
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Permisson checks for class based views
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_customers = Customer.objects.all().count()
    num_systems = System.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_customers': num_customers,
        'num_systems': num_systems,
        'num_visits' : num_visits
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class CustomerListView(generic.ListView):
    model = Customer
    context_object_name = 'customer_list'
    template_name = 'catalog_app/customer_list'
    paginate_by = 10

    def get_queryset(self):
        return Customer.objects.all()

class CustomerDetailView(generic.DetailView):
    model = Customer
    paginate_by = 2
 
class SystemListView(generic.ListView):
    model = System
    context_object_name = 'system_list'
    template_name = 'catalog_app/system_list'
    paginate_by=10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(SystemListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['test_column'] = 'Testing additional variable'
        return context
  
class SystemDetailView(generic.DetailView):
    model = System

############################### Handling Post requests ####################################

@login_required
@permission_required('catalog_app.can_see_all_customers', raise_exception=True)
def renew_customer(request, pk):
    customer_instance = get_object_or_404(Customer, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = UpdateCustomerForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            customer_instance.location = form.cleaned_data['new_location']
            customer_instance.save()

            # redirect to a new URL (HomePage):
            return HttpResponseRedirect(reverse('customer-detail', args=[pk]) )

    # If this is a GET (or any other method) create the default form.
    else:
        form = UpdateCustomerForm(initial={'new_location': customer_instance.location})

    context = {
        'form': form,
        'customer_instance': customer_instance,
    }

    return render(request, 'catalog_app/update_customer.html', context)

############################### CRUD Operations ####################################

class SystemCreate(CreateView):
    model = System
    fields = ['customer', 'protocol', 'host', 'suffix', 'port', 'user', 'password', 'token']
    initial = {'customer': 'Demo Customer'}

class SystemUpdate(UpdateView):
    model = System
    fields = ['customer', 'protocol', 'host', 'suffix', 'port', 'user', 'password', 'token']

class SystemDelete(DeleteView):
    model = System
    success_url = reverse_lazy('systems')


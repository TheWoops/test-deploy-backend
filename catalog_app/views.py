from django.shortcuts import render
from django.views import generic

# Create your views here.
from catalog_app.models import Customer, System

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_customers = Customer.objects.all().count()
    num_systems = System.objects.all().count()

    context = {
        'num_customers': num_customers,
        'num_systems': num_systems,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class CustomerListView(generic.ListView):
    model = Customer
    context_object_name = 'customer_list'
    template_name = 'catalog_app/customer_list'
    paginate_by = 1

    def get_queryset(self):
        return Customer.objects.all()

class CustomerDetailView(generic.DetailView):
    model = Customer
    paginate_by = 2
 
class SystemListView(generic.ListView):
    model = System
    context_object_name = 'system_list'
    template_name = 'catalog_app/system_list'
    queryset = System.objects.all()[:3]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(SystemListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['test_column'] = 'Testing additional variable'
        return context
   
class SystemDetailView(generic.DetailView):
    model = System
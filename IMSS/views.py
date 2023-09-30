from django.shortcuts import get_object_or_404, render , HttpResponse ,HttpResponse, redirect
from .models import Inventory
from django.contrib.auth.decorators import login_required
from .forms import InventoryUpdateForm, AddInventoryForm
from django.contrib import messages
from django_pandas.io import read_frame
import plotly
import plotly.express as px
import json



@login_required
def inventory_list(request):
    inventories = Inventory.objects.all()
    context = {
        "inventories": inventories
    }
    return render(request, "inventory/inventory_list.html", context=context)


@login_required
def per_product(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context = {
        'inventory': inventory
    }
    return render(request, "inventory/per_product_view.html", context=context)

def product_update(request):
    return HttpResponse ("hello")


@login_required()
def add_product(request):
    if request.method == "POST":
        updateForm = AddInventoryForm(data=request.POST)
        if updateForm.is_valid():
            new_invetory = updateForm.save(commit=False)
            new_invetory.sales = float(updateForm.data['cost_per_item']) * float(updateForm.data['quantity_sold'])
            new_invetory.save()
            
            
            return redirect(f"/inventory/")
    else:
        updateForm = AddInventoryForm()

    return render(request, "inventory/inventory_add.html", {'form' : updateForm})


@login_required()
def delete(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    inventory.delete()
    
    return redirect("/inventory/")


@login_required()
def update(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        updateForm = InventoryUpdateForm(data=request.POST)
        if updateForm.is_valid():
            inventory.name = updateForm.data['name']
            inventory.quantity_in_stock = updateForm.data['quantity_in_stock']
            inventory.quantity_sold = updateForm.data['quantity_sold']
            inventory.cost_per_item = updateForm.data['cost_per_item']
            inventory.sales = float(inventory.cost_per_item) * float(inventory.quantity_sold)
            inventory.save()
            
            return redirect(f"/inventory/per_product_view/{pk}")
    else:
        updateForm = InventoryUpdateForm(instance=inventory)

    return render(request, "inventory/inventory_update.html", {'form' : updateForm})


    
# @login_required()
# def dashboard(request):
#     inventories = Inventory.objects.all()
#     df = read_frame(inventories)
    
#     # sales graph
#     #print(df.columns)
#     sales_graph_df = df.groupby(by="last_sale_date", as_index=False, sort=False)['sales'].sum()
#     #print(sales_graph_df.sales)
#     ##print(sales_graph_df.columns)
#     sales_graph = px.line(sales_graph_df, x = sales_graph_df.last_sale_date, y = sales_graph_df.sales, title="Sales Trend")
#     sales_graph = json.dumps(sales_graph, cls=plotly.utils.PlotlyJSONEncoder)
    
#     context = {
#         "sales_graph": sales_graph,

#     }
#     print (sales_graph)

#     return render(request,"inventory/dashboard.html", context=context)
@login_required
def dashboard(request):
    #  = Order.objects.all()
    # if request.method=='POST':
    #     form = (request.POST)
    #     if form.is_valid():
    #         instance=form.save(commit=False)
    #         instance.staff = request.user
    #         instance.save()
    #         redirect('dashboard-index')
    # else:
    #     form = O()
    # context = {
    #     'orders':orders,
    #     'form':form,
    # }
    return render(request,"inventory/dashboard.html",)
from django.shortcuts import render,get_object_or_404
from .models import Project,project_formal,project_casual,project_reviews,footer

# Create your views here.

def project(request):
    var_1 = Project.objects.all()
    var_2 = project_formal.objects.all()
    var_3 = project_casual.objects.all()
    var_4 = project_reviews.objects.all()
    var_5 = footer.objects.all()
    return render(request, 'project/bootstrap.html',
                  {'var_1':var_1,'var_2':var_2,'var_3':var_3,'var_4':var_4,'var_5':var_5}
                  )


def single(request, project_id):
    single_var = get_object_or_404(project_formal, pk=project_id)
    single_var2 = get_object_or_404(project_casual, pk=project_id)
    return render(request, 'project/single_product.html', {'single_var': single_var,'single_var2': single_var2})



# can remove
def base(request):
    base_var = footer.objects.all()
    return render(request, 'project/base.html',{'base_var':base_var})



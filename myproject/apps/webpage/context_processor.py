from .models import Testimoni

# Create your views here.
def testimonis(request):
    testimonis = Testimoni.objects.all()

    return {'testimonis': testimonis}

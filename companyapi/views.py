from django.http import JsonResponse


def home_page(request):
    print("home page requested")
    employee = {
        'e_id' : 1001,
        'name' : 'Richard Nixon'
    }
    return JsonResponse(employee, safe=False)

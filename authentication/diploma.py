import json
from django.http import JsonResponse
from authentication.models import Diploma, UserProf
from rest_framework.decorators import api_view

@api_view(['POST'])
def diploma_create(request):
    if request.method == "POST":
        try:
            data = request.data

            prof_email = data.get("prof_email")
            professor = UserProf.objects.get(email=prof_email)

            dip_name = data.get("diploma_name")
            s_date = data.get("start_date")
            e_date = data.get("end_date")

            diploma = Diploma.objects.create(
                user_prof=professor, name=dip_name, start_date=s_date, end_date=e_date
            )

            return JsonResponse({"message": "diploma createg successfully"}, status=200)
        except KeyError:
            return JsonResponse({"error": "Missing required fields"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

@api_view(['GET'])
def diploma_read(request):
    if request.method == "GET":
        prof_email = request.GET.get("prof_email")
        dip_name = request.GET.get("dip_name")
        professor = UserProf.objects.get(email=prof_email)
        if professor and dip_name:
            try:
                diplomas = Diploma.objects.get(user_prof=professor, name=dip_name)
                return JsonResponse(diplomas, status=200)
            except Diploma.DoesNotExist:
                return JsonResponse({"error": "Diploma not found"}, status=404)
        else:
            return JsonResponse({"error": "Name parameter is missing"}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

@api_view(['PUT'])
def diploma_update(request):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            diploma_id = data.get("id")
            if diploma_id is not None:
                diploma = Diploma.objects.get(pk=diploma_id)

                diploma.name = data.get("name")
                diploma.date = data.get("date")

                diploma.save()
                return JsonResponse({"message": "diploma updated successfully"})
            else:
                return JsonResponse({"error": "diploma ID is missing"}, status=400)
        except Diploma.DoesNotExist:
            return JsonResponse({"error": "diploma not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

@api_view(['DELETE'])
def diploma_delete(request):
    if request.method == "DELETE":
        prof_email = request.GET.get("prof_email")
        dip_name = request.GET.get("dip_name")
        professor = UserProf.objects.get(email=prof_email)
        if professor and dip_name:
            try:
                diploma = Diploma.objects.get(user_prof=professor, name=dip_name)
                diploma.delete()
                return JsonResponse({"message": "Diploma deleted successfully"}, status=200)
            except Diploma.DoesNotExist:
                return JsonResponse({"error": "Diploma not found"}, status=404)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

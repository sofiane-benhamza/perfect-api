from django.http import JsonResponse
import json
from  authentication.models import ReviewsProf, UserProf, UserStudent
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view

@api_view(['POST'])
def review_create(request):
    if request.method == 'POST':
        try:
            data = request.data
            scorer_email = data.get('scorer_email') 
            user_prof_email = data.get('user_prof_email')
            given_score = data.get('given_score')
            date = data.get('date')

            user_prof = UserProf.objects.get(email=user_prof_email)
            scorer = UserStudent.objects.get(email=scorer_email)
            review = ReviewsProf.objects.create(user_prof=user_prof,scorer = scorer, given_score=given_score, date=date)

            return JsonResponse({'message': 'Review created successfully'}, status=200)
        except KeyError:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'UserProf not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['GET'])
def review_read(request, review_id):
    if request.method == 'GET':   
        try:
            email = request.data.get("email")
            reviews = ReviewsProf.objects.get(email=email)
            return JsonResponse({reviews}, status=200)
        except ReviewsProf.DoesNotExist:
            return JsonResponse({'error': 'Reviews not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@api_view(['PUT'])
def review_update(request):
    if request.method =='PUT':
        try:
            data = request.data
            prof_email = data.get('user_prof_email')
            scorer_email = data.get('scorer_email')
            given_score = data.get('given_score')
            date = data.get('date')

            scorer = UserStudent.objects.get(email = scorer_email)

            review = ReviewsProf.objects.get(user_prof=prof_email, scorer=scorer)
            review.given_score = given_score
            review.date = date
            review.save()

            return JsonResponse({'message': 'Review updated successfully'})
        except ReviewsProf.DoesNotExist:
            return JsonResponse({'error': 'Review not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@api_view(['DELETE'])
def review_delete(request, review_id):
    if request.method == 'DELETE':
        try:
            scorer_email = request.data.get("scorer_email")
            scorer = UserStudent.objects.get(email=scorer_email)
            review = ReviewsProf.objects.get(scorer=scorer)
            review.delete()

            return JsonResponse({'message': 'Review deleted successfully'})
        except ReviewsProf.DoesNotExist:
            return JsonResponse({'error': 'Review not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
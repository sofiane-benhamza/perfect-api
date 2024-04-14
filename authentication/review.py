from django.http import JsonResponse
import json
from  authentication.models import ReviewsProf, UserProf
from django.core.exceptions import ObjectDoesNotExist


def review_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_prof_id = data.get('user_prof_id')
            given_score = data.get('given_score')
            date = data.get('date')

            user_prof = UserProf.objects.get(pk=user_prof_id)
            review = ReviewsProf.objects.create(user_prof=user_prof, given_score=given_score, date=date)

            return JsonResponse({'message': 'Review created successfully', 'review_id': review.id})
        except KeyError:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'UserProf not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def review_read(request, review_id):
    if request.method == 'GET':
        try:
            review = ReviewsProf.objects.get(pk=review_id)
            data = {
                'id': review.id,
                'given_score': review.given_score,
                'date': review.date,
                'user_prof_id': review.user_prof_id
            }
            return JsonResponse({'review': data})
        except ReviewsProf.DoesNotExist:
            return JsonResponse({'error': 'Review not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def review_update(request, review_id):
    if request.method =='PUT':
        try:
            data = json.loads(request.body)
            given_score = data.get('given_score')
            date = data.get('date')
            user_prof_id = data.get('user_prof_id')

            review = ReviewsProf.objects.get(pk=review_id)
            review.given_score = given_score
            review.date = date
            review.user_prof_id = user_prof_id
            review.save()

            return JsonResponse({'message': 'Review updated successfully'})
        except ReviewsProf.DoesNotExist:
            return JsonResponse({'error': 'Review not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def review_delete(request, review_id):
    if request.method == 'DELETE':
        try:
            review = ReviewsProf.objects.get(pk=review_id)
            review.delete()

            return JsonResponse({'message': 'Review deleted successfully'})
        except ReviewsProf.DoesNotExist:
            return JsonResponse({'error': 'Review not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
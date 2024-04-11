from django.http import JsonResponse
from  authentication.models import ReviewsProf, UserProf
from django.core.exceptions import ObjectDoesNotExist


def  review_create(request):
    if request.method == 'POST':
        given_score = request.POST.get('given_score')
        date = request.POST.get('date')
        user_prof_id = request.POST.get('user_prof_id')
        try:
            user_prof = UserProf.objects.get(pk=user_prof_id)
            review = ReviewsProf.objects.create(given_score=given_score, date=date, user_prof=user_prof)
            return JsonResponse({'message': 'Review created successfully', 'id': review.id})
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'UserProf not found'}, status=404)
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
    if request.method in ['PUT', 'PATCH']:
        given_score = request.POST.get('given_score')
        date = request.POST.get('date')
        user_prof_id = request.POST.get('user_prof_id')
        try:
            review = ReviewsProf.objects.get(pk=review_id)
            review.given_score = given_score
            review.date = date
            review.user_prof_id = user_prof_id
            review.save()
            return JsonResponse({'message': 'Review updated successfully'})
        except ReviewsProf.DoesNotExist:
            return JsonResponse({'error': 'Review not found'}, status=404)
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
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

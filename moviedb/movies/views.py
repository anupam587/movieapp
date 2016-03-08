from django.shortcuts import render
from django.db.models import Q
import datetime
#from .forms import SignUpForm
from .models import Movie
from .models import Category

# Create your views here.
def home(request):
	title = 'Movies Home'
	user = request.user

	#form = SignUpForm(request.POST or None)
	upcoming_movies = Movie.objects.filter(Q(release_date__gte = datetime.datetime.today()))
	start_day = datetime.datetime.today() - datetime.timedelta(300)
	last_day = datetime.datetime.today()
	latest_movies = Movie.objects.filter(Q(release_date__range = (start_day, last_day)))
	mixcategory = Category.objects.all()
	toprated_movies = Movie.objects.order_by('-ratings')[:3]

	category_movies = []
	for category in mixcategory:
		category_movie_details = Movie.objects.filter(Q(categories__name = category.name))
		category_movie_name = category.name
		category_movie = {
			"name" : category_movie_name,
			"details" : category_movie_details,
		}
	 	category_movies.append(category_movie)
   
    
	upcoming_movie_list = []
	latest_movie_list = []
	category_movies_list = []
	toprated_movies_list = []

	for x in upcoming_movies:
		print x.director
		movie_obj = {
		    "title" : x.title,
		    "director" : x.director,
		    "cast" : x.casts.all,
		    "release_date" : str(x.release_date),
		    "description" : x.description,
		    "rating" : x.ratings,
		    "picpath" : x.trailerimg
		}
		#print x.release_date
		upcoming_movie_list.append(movie_obj)


	for x in latest_movies:
		movie_obj = {
		    "title" : x.title,
		    "director" : x.director,
		    "cast" : x.casts.all,
		    "release_date" : str(x.release_date),
		    "description" : x.description,
		    "rating" : x.ratings,
		    "picpath" : x.trailerimg
		}
		#print x.release_date
		latest_movie_list.append(movie_obj)	

	for x in toprated_movies:
		movie_obj = {
		    "title" : x.title,
		    "director" : x.director,
		    "cast" : x.casts.all,
		    "release_date" : str(x.release_date),
		    "description" : x.description,
		    "rating" : x.ratings,
		    "picpath" : x.trailerimg
		}
		#print x.release_date
		toprated_movies_list.append(movie_obj)

	context = {
	   "title" : title,
	   "user" : user,
	   "upcoming_movie_list" : upcoming_movie_list,
	   "latest_movie_list" : latest_movie_list,
	   "toprated_movies_list" : toprated_movies_list,
	   "category_movies_list" : category_movies,
 	}

	return render(request, 'home.html', context)


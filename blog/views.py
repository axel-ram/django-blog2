from django.shortcuts import render
posts = [
	{
		'author': 'Ramnath',
		'title': 'How to create templated in django',
		'content': 'Content is coming soon',
		'date_posted': 'September 15, 2020'
	},
	{
		'author': 'Tanmay',
		'title': 'How to do competitive programming',
		'content': 'Content will be upated soon',
		'date_posted': 'September 11, 2020'
	},
]

# Create your views here.
def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

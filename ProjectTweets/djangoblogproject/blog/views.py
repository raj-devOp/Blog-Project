from django.shortcuts import render


posts = [
    {
        'Author': 'Raj P',
        'Title': 'Python Django Tutorial',
        'Content': 'My first Python Web App',
        'Date_posted': 'March 7, 2023'
    },

    {
        'Author': 'Harry Potter',
        'Title': 'Hogwards is Real',
        'Content': 'Why I love to become a Wizard',
        'Date_posted': 'April 8, 2023'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


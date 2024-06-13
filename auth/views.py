from django.shortcuts import render

def home(request):
    images, favourite_list = []
    return render(request, 'home.html', {'images': images, 'favourite list': favourite_list})
    
def getAllImagesAndFavouriteList(request):
    images = []
    favourite_list = []

    return images, favourite_list
    
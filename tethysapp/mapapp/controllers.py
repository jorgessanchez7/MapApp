from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button
from tethys_sdk.gizmos import *
import csv, os
from datetime import datetime
import random
import string
from tethys_sdk.services import get_spatial_dataset_engine
import urlparse

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    save_button = Button(
        display_text='',
        name='save-button',
        icon='glyphicon glyphicon-floppy-disk',
        style='success',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Save'
        }
    )

    edit_button = Button(
        display_text='',
        name='edit-button',
        icon='glyphicon glyphicon-edit',
        style='warning',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Edit'
        }
    )

    remove_button = Button(
        display_text='',
        name='remove-button',
        icon='glyphicon glyphicon-remove',
        style='danger',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Remove'
        }
    )

    previous_button = Button(
        display_text='Previous',
        name='previous-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Previous'
        }
    )

    next_button = Button(
        display_text='Next',
        name='next-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Next'
        }
    )

    context = {
        'save_button': save_button,
        'edit_button': edit_button,
        'remove_button': remove_button,
        'previous_button': previous_button,
        'next_button': next_button
    }

    return render(request, 'mapapp/home.html', context)

def proposal(request):
    """
    Scores page for my App
    """

    context ={

    }

    return render(request, 'mapapp/proposal.html', context)

def mockup(request):
    """
    Scores page for my App
    """

    context ={

    }

    return render(request, 'mapapp/mockup.html', context)

def mapview(request):
    """
    Scores page for my App
    """

    context ={

    }

    return render(request, 'mapapp/mapview.html', context)

def dataservices(request):
    """
    Scores page for my App
    """

    context ={

    }

    return render(request, 'mapapp/dataservices.html', context)


def about(request):
    """
    Scores page for my App
    """

    context ={

    }

    return render(request, 'mapapp/about.html', context)
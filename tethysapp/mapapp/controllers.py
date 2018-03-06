from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button
from tethys_sdk.gizmos import DatePicker
from tethys_sdk.gizmos import TimeSeries
from tethys_sdk.gizmos import SelectInput
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
    date_picker_initial = DatePicker(name='date1',
                             display_text='Initial Date',
                             autoclose=True,
                             format='MM d, yyyy',
                             start_date='1/1/2000',
                             start_view='decade',
                             today_button=False,
                             initial='January 1, 2018')

    date_picker_final = DatePicker(name='date2',
                             display_text='Final Date',
                             autoclose=True,
                             format='MM d, yyyy',
                             start_date='1/2/2000',
                             start_view='decade',
                             today_button=True,
                             initial='March 1, 2018')

    select_input = SelectInput(display_text='Download',
                               name='select1',
                               multiple=False,
                               original=True,
                               options=[('As txt', '1'), ('As csv', '2'), ('As xls', '3')],
                               initial=['As txt'])

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Irregular Timeseries Plot',
        y_axis_title='Snow depth',
        y_axis_units='m',
        series=[{
            'name': 'Winter 2007-2008',
            'data': [
                [datetime(2008, 12, 2), 0.8],
                [datetime(2008, 12, 9), 0.6],
                [datetime(2008, 12, 16), 0.6],
                [datetime(2008, 12, 28), 0.67],
                [datetime(2009, 1, 1), 0.81],
                [datetime(2009, 1, 8), 0.78],
                [datetime(2009, 1, 12), 0.98],
                [datetime(2009, 1, 27), 1.84],
                [datetime(2009, 2, 10), 1.80],
                [datetime(2009, 2, 18), 1.80],
                [datetime(2009, 2, 24), 1.92],
                [datetime(2009, 3, 4), 2.49],
                [datetime(2009, 3, 11), 2.79],
                [datetime(2009, 3, 15), 2.73],
                [datetime(2009, 3, 25), 2.61],
                [datetime(2009, 4, 2), 2.76],
                [datetime(2009, 4, 6), 2.82],
                [datetime(2009, 4, 13), 2.8],
                [datetime(2009, 5, 3), 2.1],
                [datetime(2009, 5, 26), 1.1],
                [datetime(2009, 6, 9), 0.25],
                [datetime(2009, 6, 12), 0]
            ]
        }]
    )

    context = {
        'date_picker_initial': date_picker_initial,
        'date_picker_final': date_picker_final,
        'select_input': select_input,
        'timeseries_plot': timeseries_plot,
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


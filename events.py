from flask import Blueprint, render_template, request, redirect, url_for
#from .models import Destination, Comment
#from .forms.py import EventForm, ReviewForm
from . import UPLOAD_FOLDER, db
import os
from werkzeug.utils import secure_filename

# This is where our blueprints will go
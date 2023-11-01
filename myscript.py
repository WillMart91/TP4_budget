import os
import sys
sys.stdout.flush()
os .system ('git bisect start c1a4be0 e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c')
os .system ('git bisect run python manage.py test')
#!/usr/bin/env python

import os
import sys
import yaml

class Base(object):

  def __init__(self):
    """ inits common vars """
    self.conf = yaml.load(file('conf.yaml', 'r'))

  def _display_progress(self, **kwargs):
    """ Progress bar :
      kwargs['curr']
        current loop index, starts with 1
      kwargs['total']
        total number of iterations in a loop
      kwargs['progress_for']
        (optional) progress bar description (free-form text)
    """
    if kwargs['curr'] == 1:
      self.progress = ['0.' + str(i).zfill(2) for i in range(1, 100)] + ['1.00']
      progress_for_str = ' [ %s ] ' % (kwargs['progress_for']) if kwargs.get('progress_for', None) else ''
      sys.stdout.write('\nProgress%s: ' % (progress_for_str))
      sys.stdout.flush()
    if len(self.progress):
      curr = float(kwargs['curr']) / float(kwargs['total'])
      less = [i for i in self.progress if float(i) <= curr]
      for i, item in enumerate(less):
        sys.stdout.write('.')
        sys.stdout.flush()
      self.progress = self.progress[len(less):]
      if not len(self.progress):
        sys.stdout.write(' [ ' + str(kwargs['total']) + ' total, 100% ] \n')
        sys.stdout.flush()

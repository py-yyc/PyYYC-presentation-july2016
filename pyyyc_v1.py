from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from six import string_types


class PyYYCPresentation(object):
    """ class PyYYCPresentation

    This class contains info about basic presentations at the
    PyYYC meetup. It generates some really useful summary info
    about the presentation.

    Inputs:
        presenter   - Name of the presenter
        topic       - Brief explanation of the topic
        time_limit  - Time limit of the presentation
        nslides     - Number of slides (because all presentations
                      have slides!)
        slide_color - RGB color of all the slides
    """

    def __init__(self, presenter, topic, time_limit, nslides, slide_color):
        self.set_presenter(presenter)
        self.set_topic(topic)
        self.set_time_limit(time_limit)
        self.set_nslides(nslides)
        self.set_slide_color(slide_color)

    def set_presenter(self, value):
        if not isinstance(value, string_types):
            raise ValueError('{}: presenter must be string'.format(value))
        self.presenter = value

    def set_topic(self, value):
        if not isinstance(value, string_types):
            raise ValueError('{}: topic must be string'.format(value))
        self.topic = value

    def set_time_limit(self, value):
        if not isinstance(value, float):
            raise ValueError('{}: time_limit must be float'.format(value))
        self.time_limit = value

    def set_nslides(self, value):

    def set_slide_color(self, value):


    def summarize(self):
        """Print a short description of the presentation. Usefull for
        press junkets.
        """
        print('{name} talking about {topic}.'.format(
            name=self.presenter,
            topic=self.topic
        ))

    def time_per_slide(self):
        """Time available for each slide"""
        return self.time_limit / self.nslides

    def strains_eyes(self):
        """Determines if the slides will cause eye strain based on their
        color
        """
        return(any([rgb > 200 for rgb in self.slide_color]) and
               any([rgb < 50 for rgb in self.slide_color]))

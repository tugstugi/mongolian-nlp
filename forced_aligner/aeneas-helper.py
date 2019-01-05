#!/usr/bin/env python3
# coding=utf-8

"""
A wrapper for the Tacotron2 engine.
"""

from __future__ import absolute_import
from __future__ import print_function

from aeneas.language import Language
from aeneas.ttswrappers.basettswrapper import BaseTTSWrapper


class CustomTTSWrapper(BaseTTSWrapper):
    #
    # there is no Mongolian support, so use Russian
    #
    RUS = Language.RUS
    """ Russian """
    LANGUAGE_TO_VOICE_CODE = {
        RUS: "ru"
    }
    DEFAULT_LANGUAGE = RUS

    # OUTPUT_AUDIO_FORMAT = ("pcm_s16le", 1, 22050)
    #
    # aeneas seems to optimized for espeak which produce fast speeches. So fine tune the sample rate!
    #
    OUTPUT_AUDIO_FORMAT = ("pcm_f32le", 1, int(22050*0.73))

    #
    # NOTE calling eSpeak via subprocess
    #
    HAS_SUBPROCESS_CALL = True

    TAG = u"Tacotron2TTSWrapper"

    def __init__(self, rconf=None, logger=None):
        super(CustomTTSWrapper, self).__init__(rconf=rconf, logger=logger)
        self.set_subprocess_arguments([
            u"/Users/tugstugi/Projects/aligner/aeneas-helper.sh",                     # path of espeak executable or just "espeak" if it is in your PATH
            self.CLI_PARAMETER_WAVE_PATH,           # it will be replaced by the actual output file path
            self.CLI_PARAMETER_TEXT_STDIN           # text is read from stdin
        ])

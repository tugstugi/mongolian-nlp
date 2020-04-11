#!/usr/bin/env python3
# coding=utf-8

"""
A wrapper for the Kazakh espeak-ng engine.
"""
from __future__ import absolute_import
from __future__ import print_function

from aeneas.ttswrappers.basettswrapper import BaseTTSWrapper


class CustomTTSWrapper(BaseTTSWrapper):

    KAZ = "kaz"
    """Kazakh"""

    LANGUAGE_TO_VOICE_CODE = {
        KAZ: "kk"
    }
    DEFAULT_LANGUAGE = KAZ

    OUTPUT_AUDIO_FORMAT = ("pcm_s16le", 1, 22050)

    HAS_SUBPROCESS_CALL = True

    TAG = u"CustomTTSWrapper"

    def __init__(self, rconf=None, logger=None):
        super(CustomTTSWrapper, self).__init__(rconf=rconf, logger=logger)
        print(self.tts_path)
        print(self.CLI_PARAMETER_VOICE_CODE_STRING)
        self.set_subprocess_arguments([
            'espeak-ng',
            u"-v",
            u"kk",
            u"-w",
            self.CLI_PARAMETER_WAVE_PATH,
            self.CLI_PARAMETER_TEXT_STDIN
        ])

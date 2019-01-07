#!/usr/bin/env python3
# coding=utf-8

"""
A wrapper for the Tacotron2 engine.
"""

from __future__ import absolute_import
from __future__ import print_function

from aeneas.ttswrappers.basettswrapper import BaseTTSWrapper

from os import path

tacotron2_synthesizer_path = path.join(path.dirname(path.realpath(__file__)), 'aeneas-helper.sh')


class CustomTTSWrapper(BaseTTSWrapper):

    MON = "mon"
    """Mongolian"""

    LANGUAGE_TO_VOICE_CODE = {
        MON: "mn"
    }
    DEFAULT_LANGUAGE = MON

    # OUTPUT_AUDIO_FORMAT = ("pcm_s16le", 1, 22050)
    #
    # aeneas seems to optimized for espeak which produce fast speeches. So fine tune the sample rate!
    #
    OUTPUT_AUDIO_FORMAT = ("pcm_f32le", 1, int(22050 * 0.73))

    #
    # NOTE calling Tacotron2 via subprocess
    #
    HAS_SUBPROCESS_CALL = True

    TAG = u"Tacotron2TTSWrapper"

    def __init__(self, rconf=None, logger=None):
        super(CustomTTSWrapper, self).__init__(rconf=rconf, logger=logger)
        self.set_subprocess_arguments([
            tacotron2_synthesizer_path,
            self.CLI_PARAMETER_WAVE_PATH,  # it will be replaced by the actual output file path
            self.CLI_PARAMETER_TEXT_STDIN  # text is read from stdin
        ])

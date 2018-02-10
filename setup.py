#!/usr/bin/env python

from __future__ import print_function
import sys, unittest
from distutils.core import setup, Command

class Test(Command):
    description = "run tests"
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        test = unittest.defaultTestLoader.discover("pure25519_blake2b")
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(test)
        sys.exit(not result.wasSuccessful())

class KnownAnswerTest(Test):
    description = "run known-answer-tests"
    def run(self):
        test = unittest.defaultTestLoader.loadTestsFromName("pure25519_blake2b.do_ed25519_kat")
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(test)
        sys.exit(not result.wasSuccessful())

class Speed(Test):
    description = "run benchmark suite"
    def run(self):
        from pure25519_blake2b import speed_basic, speed_ed25519, speed_dh, speed_spake2
        speed_basic.run()
        speed_ed25519.run()
        speed_dh.run()
        speed_spake2.run()

setup(name="pure25519_blake2b",
      version="0", # not for publication
      description="pure-python curve25519/ed25519 routines",
      author="Brian Warner",
      author_email="warner-python-pure25519_blake2b@lothar.com",
      license="MIT",
      url="https://github.com/warner/python-pure25519_blake2b",
      packages=["pure25519_blake2b"],
      package_dir={"pure25519_blake2b": "pure25519_blake2b"},
      cmdclass={"test": Test, "speed": Speed, "test_kat": KnownAnswerTest},
      )

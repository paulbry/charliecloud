Synopsis
========

::

  $ ch-test [OPTION..] ARG

Description
===========

Run the charliecloud test suite.

Options
=======

  :code:`-t`, :code:`--tar-dir=DST`
    Set the tarball directoy to path `DST`. Equivilant to setting CH_TEST_TARDIR
    to :code:`DST` (by default :code: `DST` is :code:`/var/tmp/tar`)

  :code:`-i`, :code:`--img-dir=DST`
    Set the image directoy to path `DST`. Equivilant to setting CH_TEST_IMGDIR
    to :code:`DST` (by default :code: `DST` is :code:`/var/tmp/img`).

  :code:`-s`, :code:`--scope=SCOPE`
    Set the scope of the charliecloud test suite to :code:`SCOPE`. Equivilant to
    setting CH_TEST_SCOPE to :code:`SCOPE` (by default :code:`SCOPE` is
    :code:`standard`).

  :code:`-p`, :code:`--perm-dirs='ARG'`
    Specify the directories :code:`'ARG'` for file permission enforcement tests
    (by default :code:`'ARG'` is :code:`'/var/tmp /tmp'`).

  :code:`-c`, :code:`--clean`
    Clean docker image cache. Required sudo.

Arguments
=========

  :code: `build`
    Test image building and associated functionality.

  :code: `run`
    Test images with charliecloud runtime. Requires the contents of
    :code:`CH_TEST_TARDIR` produced by a successful :code:`ch-test build`.

  :code: `examples`
    Run examples. Depends on successful :code:`ch-test run`
    
  :code: `perms`
    Run permissions tests. Depends on successful :code:`ch-test build`

Example
=======

::

  $ ch-test build
  CH_TEST_TARDIR empty, using /var/tmp/tar
  CH_TEST_IMGDIR empty, using /var/tmp/img
  CH_TEST_PERMDIRS empty, using '/var/tmp tmp'
  CH_TEST_SCOPE empty, using standard

  bats build.bats build_auto.bats build_post.bats
  ✓ create tarball directory if needed
  ✓ documentations build
  ✓ version number seems sane
  ✓ executables seem sane
  ...
  ...

.. aiogifs documentation master file, created by
   sphinx-quickstart on Fri May 28 00:32:00 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to aiogifs's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
   tenor
   giphy


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`




Getting Started
===============

Lets take a look at some basic examples with the Tenor Client first:

.. code-block:: python

   from aiogifs.tenor import TenorClient

   client = TenorClient(api_key = "TENOR_API_KEY")
   resp = await client.search("cats")
   first_media = resp[0]
   print(first_media.url)


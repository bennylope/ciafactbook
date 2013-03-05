CIA World Factbook: Haystack demonstration
==========================================

This project shows some Haystack functionality by doing "the same thing"
in several different ways.

It is set up to deploy to Heroku with only some minimal configuration.

After creating your Heroku app (and syncing your database) you'll need
to add ElasticSearch. For the Bonsai add-on::

    heroku addons:add bonsai:starter

Next, you need to initiate the index::

    curl -XPOST http://mepnlrtt:senz9n07uf1vvgly@oak-3071254.us-east-1.bonsai.io/haystack

That's the form of::

    curl -XPOST http://<user>:<password>@<host>/<chosen-index-name>

Now you can build your index::

    heroku run python manage.py update_index

# wordzlet
wordzlet = Vocab + Merriam-Webster Definition + Quizlet API

## To Use
 - First you'll need to have a Quizlet API Access token. Quizlet uses OAuth2 so you'll first have to exchange your application credentials for an access token to use the private functionalities. [This page](https://quizlet.com/api/2.0/docs/oauth-example-php) provides a pretty convenient way to grab the stuffs you'll need using a generated php script. Note that you'll have to have a public-facing IP-address to do that.
 - Copy over `_settings.py.example` to `_settings.py` and make sure everything fits your needs.
 - Run `wordzlet.py` and go check your quizlet page. Anything new?
 
## License
Released under the MIT License.

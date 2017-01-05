# wordzlet
wordzlet = Vocab + Merriam-Webster Definition + Quizlet API

## To Use
 - First you'll need to have a Quizlet API Access token. Quizlet uses OAuth2 so you'll first have to exchange your application credentials for an access token to use the private functionalities. [This page](https://quizlet.com/api/2.0/docs/oauth-example-php) provides a pretty convenient way to grab the stuffs you'll need using a generated php script. Note that you'll have to have a public-facing IP-address to do that.
 - Copy over `_settings.py.example` to `_settings.py` and make sure everything fits your needs.
 - Run `wordzlet.py` and go check your quizlet page. Anything new?

**Dictionary used: [adambom/dictionary: English Language Dictionary](https://github.com/adambom/dictionary)**

## Known issues
 - The json-version Merriam-Webster dictionary used doesn't recognize all forms of a word - outputs -1 and requires manual modification on a few cases.
 - the json-version dictionary needs to be fetched from a url everytime the script runs
 - the json-version dictionary provides very, very verbose definitions

## Effect
 - [testfile.txt](https://quizlet.com/178733991/dynamiccachetestfiletxt-flash-cards/)
 - [holt1-8.txt](https://quizlet.com/178734153/dynamiccacheholt1-8txt-flash-cards/)
 - [holt9-16.txt](https://quizlet.com/178734283/dynamiccacheholt9-16txt-flash-cards/)

## License
Released under the MIT License.

# Universal-DB
> An online database of 3DS and DS homebrew

[![Crowdin](https://badges.crowdin.net/universal-db/localized.svg)](https://crowdin.com/project/universal-db)

## Uses
- https://db.universal-team.net, hosted from this repository with GitHub Pages this is the official Universal-DB website
- [Universal-Updater](https://github.com/Universal-Team/Universal-Updater), Universal-DB is the default UniStore of Universal-Updater
- [Universal-Bot](https://github.com/Universal-Team/Universal-Bot), our Discord bot, with `?db` you can search for apps on Universal-DB
- [UDB-API](https://github.com/LightSage/UDB-API) by [LightSage](https://github.com/LightSage), a proper API for Universal-DB

## Supported sites for automatic data collection
These sites are the preferred places to host your downloads as Universal-DB can automatically fetch most of the info about it. More sites can be added provided they have sufficient info about it and are easy enough to get that info from, prefereably having some kind of API for it.

- [GitHub](https://github.com): Full support
- [Bitbucket](https://bitbucket.org): Partial support
- [Gitlab](https://gitlab.com): Partial support

## Using the data
As Universal-DB is hosted by GitHub pages we're not able to have a proper API, but you can use `docs/data/full.json` to get all the data we collect from the GitHub API and such all in one place or LightSage's [UDB-API](https://udb-api.lightsage.dev) for an unofficial proper API. If using `full.json`, it can be accessed from https://db.universal-team.net/data/full.json.
Please make an issue here or ask on [our Discord server](https://universal-team.net/discord) if you would like anything to be added to `full.json`, if possible we will try add it.

It would be nice if you credit us if you use our data, just a link to this repo or the official website with something like "Data from [Universal-DB](https://github.com/Universal-Team/db)" or so would be fine.

## Running the data collection
Universal-DB is updated automatically every hour / 6 hours (depending on the app's priority) using GitHub Actions, however if you would like to run the data collection and file generation yourself then you will need to:
1. Install `tex3ds` and `grit` using [devkitPro's pacman](https://devkitpro.org/wiki/Getting_Started)
   - These are needed to generate the t3x files for the Universal-Updater's UniStore
1. Install a recent version of [Python 3](https://www.python.org)
1. Open a terminal window in the `source` folder of this repository
1. Run `pip3 install -r requirements.txt` to install the needed Python libraries
1. Run `python3 generate.py`
   - You can pass a GitHub API token as the first argument to expand your API rate limit, this is needed with the default apps
   - You can pass `priority` as the second argument to only update apps updated in the last 30 days

The JSON files in `source/apps` is where the base data comes from, all apps should have a `github` (user/repo string), `systems` (string array), `categories` (string array), `image` (url string), and `icon` (url string). If the app isn't on GitHub then you will need to fill out most of the other information too. Some info can be pulled from the Bitbucket API too, but it's a bit more complicated than GitHub, look for examples in the current files. If `priority` is `true` then the app will be checked hourly by actions instead of every 6 hours, technically everything could be done hourly but due to the amount of apps that rarely update it's done every 6 to reduce spam on GitHub's API.
All info in `full.json` can override the GitHub API by specifying it in a source JSON, for example if you want an app title to have a space instead of a hyphen.

Running `generate.py` will generate the following files:
- A markdown file for each 3DS app in `docs/_3ds`
- A markdown file for each DS app in `docs/_ds`
- `docs/data/full.json`, a JSON with all collected info
- `docs/unistore/universal-db.unistore`, a UniStore format file for Universal-Updater
- `docs/unistore/universal-db.t3x`, a t3x format spritesheet for Universal-Updater

## Running the site locally
All of the website files are stored in the `docs` folder. To test the site locally, install Jekyll by running:
```
gem install bundler jekyll
```
Then run
```
bundle install
```
Then you can run the site by running this in the `docs` folder:
```
bundle exec jekyll serve
```

# Credits
- [Pk11](https://github.com/Epicpkmn11): Most website design and data collection code
- [TrianguloY](https://github.com/TrianguloY): Many of the background images, one per month
- [devkitPro](https://github.com/devkitPro): tex3ds

# Universal-DB
> An online database of 3DS and DS homebrew

## Official uses
- https://db.universal-team.net, hosted from this repository with GitHub Pages this is the official Universal-DB website
- [Universal-Updater](https://github.com/Universal-Team/Universal-Updater), Universal-DB is the default UniStore of Universal-Updater
- [Universal-Bot](https://github.com/Universal-Team/Universal-Bot), our Discord bot, with `?db` you can search for apps on Universal-DB

## Using the data
As Universal-DB is hosted by GitHub pages we're not able to have a proper API, but you can use `data/full.json` to get all the data we collect from the GitHub API and such all in one place.
Please make an issue here or ask on [our Discord server](https://universal-team.net/discord) if you would like anything to be added to `full.json`, if possible we will try add it.

It would be nice if you credit us if you use our data, just a link to this repo or the official website with something like "Data from [Universal-DB](https://github.com/Universal-Team/db)" or so would be fine.

## Running the data collection
Universal-DB is updated every 6 hours automatically using GitHub Actions, however if you would like to run the data collection and file generation yourself then you will need to:
1. Install `tex3ds` using [devkitPro's pacman](https://devkitpro.org/wiki/Getting_Started)
   - This is needed to generate the t3x files for the Universal-Updater's UniStore
1. Install a recent version of [Python 3](https://www.python.org)
1. Open a terminal window in the `source` folder of this repository
1. Run `pip3 -r requirements.txt` to install the needed Python libraries
1. Run `./generate.py`
   - You can pass a GitHub API token as the first argument to expand your API rate limit, this is needed with the default `source.json`

`source/source.json` is where the base data comes from, all apps should have a `github` (user/repo string), `systems` (string array), `categories` (string array), `image` (url string), and `icon` (url string). If the app isn't on GitHub then you will need to fill out most of the other infomation too. Some info can be pulled from the Bitbucket API too, but it's a bit more complicated than GitHub, look for examples in the current `source.json`.
All info in `full.json` can override the GitHub API by specifing it in `source.json`, for example if you want an app title to have a space instead of a hyphen.

Running `generate.py` will generate the following files:
- `index.rss`, an RSS feed of all apps updated in the last month
- A markdown file for each 3DS app in `_3ds`
- A markdown file for each DS app in `_ds`
- `data/full.json`, a JSON with all collected info
- `unistore/universal-db.unistore`, a UniStore format file for Universal-Updater
- `unistore/universal-db.t3x`, a t3x format spritesheet for Universal-Updater

# Credits
- [Pk11](https://github.com/Epicpkmn11): Most website design and data collection code
- [devkitPro](https://github.com/devkitPro): tex3ds

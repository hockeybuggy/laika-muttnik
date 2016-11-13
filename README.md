
[![Build Status](https://travis-ci.org/hockeybuggy/laika-muttnik.svg?branch=master)](https://travis-ci.org/hockeybuggy/laika-muttnik)

# Laika Muttnik

Like it's namesake, this Slackbot bold goes where no dog has been before. But
for now it mostly barks.

## Requirements

Tested on python 2.7, 3.5, or 3.6

## Install

Clone this repository to where you would like to deploy your robot. Next, create a virtualenv and source it.

    python3 -m venv .env
    source .env/bin/activate


Install dependencies:

    pip install -r requirements.txt

Run the tests:

    ./scripts/test

## Usage


Copy the example settings local and add in your slack token:

    cp .env.example .env
    vim .env

You can run the bot with:

    honcho start

## Customizing

TODO How to create your own listening bot from Slackbot.

TODO How to create your own notifier bot from Slackbot.

## Contributing

If you want to help, please do. Don't hesitate to open an issue or PR.

## TODO

- Remove the sleep usage (async python?)
- Add tests to Laika

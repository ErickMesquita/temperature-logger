# Temperature Logger

This application's goal is to practice contents learned about Docker, Python and Git.  It is an app to register my room's temperature and humidity through time. Data is obtained from an API and stored in a database.

*Read this in other languages: [Brazilian Portuguese](README.md)*

## Sampling Frequency

1 measure every 90 seconds.

## Data Source

There is a temperature and humidity sensor attached to a NodeMCU. This NodeMCU hosts a web page and an API with fixed IP address.

## Database

A SQL databse will be used, with a 3-columns table:
 - Datetime
 - Temperature
 - Humidity

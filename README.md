# Travelling Salesperson Solver

A python library to for solving real-world examples of [the travelling salesperson problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) using a brute force tree search with purning and Google Maps API to find the distances between nodes. Since this is a brute force approach it is not recommended to attempt to solve problems with more than 10 nodes.

## Installation

### Clone

Clone this repository on to you local machine using:

```bash
git clone git@github.com:btallin/travelling_salesperson_solver.git
```

### Install

From same directory, install this as a python package using [pip](https://pip.pypa.io/en/stable/):

```bash
pip install --user ./travelling_salesperson_solver
```

### Setup

Set up the configuration file with your Google maps API key.

Note: make sure that your API is authorized for use with the [Google Directions API](https://developers.google.com/maps/documentation/directions/start).

#### Option 1: Using a text editor

1. Open the file named ```travelling_salesperson_solver/.env_template``` in your text editor of choice;
2. Replace ```*place api key here*``` with your Google api.
3. Save or rename this file as ```.env```

#### Option 2: Using command line

```bash
echo API_KEY=INSERT-API-KEY-HERE > travelling_salesperson_solver/.env
```

If you do not already have a Google API key follow these [instructions](https://developers.google.com/maps/documentation/directions/get-api-key) to setup a Google Cloud account and generate a key.

As of April 2020, Google Cloud offers a promotion for new accounts so, if you're new to Google Cloud then using this API should be free for a period of time. If you're unable to setup a Google Cloud accound, generate a  API key or the cost of using this API is prohibitive for you send me an email and I will consider generating you a temperaty API from my Google account but, this will likey reserved for friends and family only.

## Usage

```python
import travelling_salesperson_solver

best_path = travelling_salesperson_solver.solve(
    addresses=(
        "The White House, Washington, DC",
        "30 Rockeffeler Plaza, New York City, New York",
        "Las Vegas Boulevard, Las Vegas, NV",
        "1600 Amphitheatre Pkwy, Mountain View, CA",
    ),
    start_anywhere=False,
    end_anywhere=False
)
print(best_path)

```

## Roadmap

* Reveal a feature to solve a problem defined by a weighted graph.
* Allow access to set the Google Direction mode. Currently it is set to 'bicycling'.
* Allow access to set the measure for travel cost between nodes. Currently using time. Another option is distance.
* Add more purning strategies to reduce the best case time. This will not change the overall time complexity or attempt to address that is is an np-hard problem.
* Add heuristic techniques using traditional programming. This will allow to for larger graphs to be solved using approximations.
* Explore heuristic techniques using mashine learning.

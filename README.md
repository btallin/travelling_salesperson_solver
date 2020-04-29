# Travelling Salesperson Solver

A python library to for solving real-world examples of [the travelling salesperson problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) using a brute force tree search with purning and Google Maps API to find the distances between nodes. Given that this is a brute force approach it is not recommended to attempt to solve problems with more than 10 nodes.

## Installation

### Clone

Clone this repository on to you local machine:

```bash
git clone git@github.com:btallin/ç.git
```

### Install

Install using [pip](https://pip.pypa.io/en/stable/) from the same directory as the previous step.

```bash
pip install --user ./travelling_salesperson_solver
```

### Setup

Set up the configuration file with your Google maps API key.

Note: make sure that your API is authorized for use with the [Google Directions API](https://developers.google.com/maps/documentation/directions/start).

#### Option 1: Using a text editor

1. Open the file named ```travelling_salesperson_solver/.env_template``` in your text editor of choice;
2. Replace ```*place api key here*``` with your Google api.

#### Option 2: Using command line

```bash
echo API_KEY=<INSERT API KEY HERE> > travelling_salesperson_solver/.env_template
```

If you do not already have a Google API key follow these [instructions](https://developers.google.com/maps/documentation/directions/get-api-key).

Google Cloud offers a promotion for new accounts making it free to use the Google Distance API and other services for a period of time. If you're unable to access a Google API key for some, send me an email and I'm might be willing to generate you a temperaty API from my Google account but, this will likey reserved for friends and family only.

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

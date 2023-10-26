
# Random Nearby Restaurant Selector

This Python script allows you to find and select nearby restaurants based on a given address using the Google Places API.

## Prerequisites

Before you can use this script, you need to install the required Python libraries and obtain a Google Places API key.

### Libraries

You can install the necessary Python libraries using pip:

`pip install requests`
`pip install geopy` 

### Google Places API Key

You need a Google Places API key to use this script. You can obtain an API key by following these steps:

1.  Visit the [Google Cloud Console](https://console.cloud.google.com/).
    
2.  Create a new project or select an existing one.
    
3.  Enable the "Google Places API" for your project.
    
4.  Create an API key in the "Credentials" section of your project.
    
5.  Copy the API key and replace `"YOUR_API_KEY"` in the script with your actual API key.
    

## Usage

To use this script, follow these steps:

1.  Run the script using your Python environment.
    
2.  Enter an address when prompted. This address will be used as the center for finding nearby restaurants.
    
3.  The script will use the Google Places API to search for restaurants near the provided address.
    
4.  It will display a randomly selected open restaurant from the list of nearby restaurants. If no open restaurants are found, it will inform you.
    

## Configuring Search Parameters

You can customize the search parameters by modifying the following variables in the script:

-   `radius`: The search radius (in meters) from the provided address.
-   `lieu_type`: The type of places to search for (e.g., "restaurant," "bakery," etc.).
-   `keyword`: Keywords used to filter the search results (e.g., "italian," "japanese," "fast_food," etc.).

Please note that this script is specifically designed to search for restaurants. If you want to search for other types of places, you can adjust the `keyword` and `lieu_type` variables accordingly.

## License

This script is provided under the [MIT License](https://chat.openai.com/c/LICENSE). Feel free to use, modify, and distribute it as needed.

Enjoy exploring and discovering nearby restaurants! 🍔🍕🌮🍣

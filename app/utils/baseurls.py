import enum

class BaseUrl(str, enum.Enum):
    """
    A base url available for retrieving data.
    """

    JHU = "https://raw.githubusercontent.com/CSSEGISandData/2019-nCoV/master/csse_covid_19_data/csse_covid_19_time_series/"
    CSBS = "https://facts.csbs.org/covid-19/covid19_county.csv"
    NYT = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"

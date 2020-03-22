from typing import List

import pandas as pd

CONFIRMED_CASES_URL = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data" \
                      f"/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv "

confirmed_cases = pd.read_csv(CONFIRMED_CASES_URL, error_bad_lines=False)


def poland_cases_by_date(day: int, month: int, year: int = 2020) -> int:
  
  rok = year % 100
  return confirmed_cases.loc[confirmed_cases["Country/Region"]=="Poland"][f"{month}/{day}/{rok}"].values[0]
   


def top5_countries_by_date(day: int, month: int, year: int = 2020) -> List[str]:
  
   
  daterino = datetime.date(year, month, day)
  daterinierononono = daterino.strftime('%m/%d/%y').lstrip("0").replace(" 0", " ").replace("/0","/")
  countries = confirmed_cases[["Country/Region", daterinierononono]].groupby(["Country/Region"]).sum().sort_values(by=daterinierononono, ascending=False).head(5)
    
  return list(countries)
   
# Function name is wrong, read the pydoc
def no_new_cases_count(day: int, month: int, year: int = 2020) -> int:
  Dait1 = datetime.date(year, month, day)
  dateOneS = dait1.strftime('%m/%d/%y').lstrip("0").replace(" 0", " ").replace("/0", "/")
  Dait2 = dait1 - datetime.timedelta(days=1)
  dateTwoS = dait2.strftime('%m/%d/%y').lstrip("0").replace(" 0", " ").replace("/0", "/")
  return len( confirmed_cases.loc[ confirmed_cases[ dateOneS ] - confirmed_cases[ dateTwoS ]!=0 ].index)

"""
F1 Race Data Extractor
---------------------
Extracts race-level and driver-level pit stop features using FastF1.

Outputs:
- Per-race CSV files
- Master CSV aggregating all races

Intended for baseline analysis and feature generation
for pit-stop strategy modeling.
"""


import fastf1
import pandas as pd
import os

fastf1.Cache.enable_cache('f1_cache')

def get_race_data(year, gp_name,save_folder='RaceData_csv'):
    try:
        session=fastf1.get_session(year, gp_name, 'R')
        session.load()
    except Exception as e:
        print(f"Skipping {gp_name} ({year}) due to session load error: {e}")
        return pd.DataFrame()
    try:
        qualifying=fastf1.get_session(year, gp_name, 'Q')
        qualifying.load()
    except Exception as e:
        print(f"Skipping qualifying for {gp_name} ({year}) due to error: {e}")
        qualifying = None
    
    race_results = session.results
    laps=session.laps
    race_name=session.event['EventName']
    print(race_name)
    no_of_laps=session.total_laps
    qualifying_results = qualifying.results

    
    race_data=[]

    for driver in session.drivers:
        drv_laps=laps.pick_drivers(driver)

        if drv_laps.empty:
            print(f"No lap data for driver {driver} in {race_name} ({year})")
            continue 

        base_lap_time = drv_laps.iloc[0]['LapTime'].total_seconds()
        drv_info=session.get_driver(driver)
        drv_code = drv_info['Abbreviation']  
        team=drv_laps['Team'].iloc[0]
        pits=drv_laps[drv_laps['PitInTime'].notna()]
        pitstop_count=len(pits)
        #fin_pos = race_results.loc[session.results['Abbreviation'] == drv_code, 'Position']
       # print(race_results)
      
        if qualifying_results is not None and not qualifying_results.empty:
            drv_qual = qualifying_results.loc[qualifying_results['DriverNumber'] == driver]
            qual_pos = int(drv_qual['Position'].iloc[0]) if not drv_qual.empty else None
        else:
            qual_pos = None


        if pitstop_count==0:
            continue

        first_pit_lap=int(pits['LapNumber'].iloc[0])
        avg_before=drv_laps[drv_laps['LapNumber']<first_pit_lap]['LapTime'].dt.total_seconds().mean()
        start_tyre=drv_laps['Compound'].iloc[0]
        after_pit_laps=drv_laps[drv_laps['LapNumber']==first_pit_lap+1]['Compound']
        after_pit = after_pit_laps.iloc[0] if not after_pit_laps.empty else None

        race_data.append(

        {
            'race_name':race_name,
            'driver_code':drv_code,
            'team_name':team,
            'no_of_laps':no_of_laps,
            'qualifying_position':qual_pos,
            'starting_tyre':start_tyre,
            'tyre_after_pit': after_pit,
            'base_lap_time':base_lap_time,
            'pitstop_count': pitstop_count, 
            'avg_lap_time_before_pit': avg_before, 
            'actual_pit_lap': first_pit_lap

        })

    
    if race_data:
        df_race = pd.DataFrame(race_data)

        # Create folder if it doesn't exist
        os.makedirs(save_folder, exist_ok=True)

        # Save CSV dynamically per race
        filename = f"{save_folder}/{year}_{race_name.replace(' ', '_')}.csv"
        df_race.to_csv(filename)
        print(f"Saved: {filename}")

        return df_race
    else:
        print(f"No valid data for {race_name} ({year}) — skipped")
        return pd.DataFrame()
 
    
def extract_data(start_year=2022, end_year=2024,save_folder='RaceData_csv'):
        all_races=[]
        for year in range(start_year, end_year + 1):
            schedule = fastf1.get_event_schedule(year)
            race_names = schedule['EventName'].tolist()
            
            for gp_name in race_names:
                    df=get_race_data(year, gp_name)
                    if df is not None and not df.empty:
                        df.insert(0,'year',year)
                        all_races.append(df)
        if all_races:
            df_final = pd.concat(all_races, ignore_index=True)
            df_final.index += 1
            master_csv = os.path.join(save_folder, 'f1_all_races_master.csv')
            df_final.to_csv(master_csv, index=False)
            print(f"\nMaster CSV saved: {master_csv}")
            return df_final
        else:
            print("No race data extracted.")
            return pd.DataFrame()
        
if __name__ == "__main__":
    extract_data()

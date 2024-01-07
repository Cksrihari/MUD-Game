import pandas as pd
import csv
from datetime import datetime, timezone  # Import timezone from datetime module
import calendar
import time

class LeaderBoard:
    def leaderBoard(self, userName, characterName, score):
        unsortedFilePath = "../resources/leaderBoard.csv"
        sortedFilePath = "../resources/sortedLeaderBoard.csv"

        current_GMT = time.gmtime()
        time_stamp = calendar.timegm(current_GMT)
        formatted_time = datetime.fromtimestamp(time_stamp, timezone.utc).strftime('%d/%m/%Y %H:%M:%S')

        # Append new data to the existing CSV file
        with open(unsortedFilePath, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([userName, characterName, score, formatted_time])

        # Read the updated CSV file and sort the data
        df = pd.read_csv(unsortedFilePath)
        sorted_df = df.sort_values(by=["Score"], ascending=False)

        sorted_df.to_csv(sortedFilePath, index=False)

        data = pd.read_csv(sortedFilePath)
        data.index = data.index + 1
        print("=" * 32 + "Leader Board" + "=" * 32)
        print()
        print(data)










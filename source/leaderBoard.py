import pandas as pd
import csv
from datetime import datetime, timezone
import calendar
import time
from extras import Extras


class LeaderBoard:
    def __init__(self):
        self.slow = Extras()

    def leader_board(self, user_name, health, score, status):

        data = open("../resources/charDetails.txt", "r")
        user_details = data.readlines()
        user_list = []
        for user in user_details:
            user = user.split(":")
            if user_name == user[0]:
                user_list.append(user)
        character_name = user_list[0][-1].strip()

        unsortedFilePath = "../resources/leaderBoard.csv"
        sortedFilePath = "../resources/sortedLeaderBoard.csv"

        current_GMT = time.gmtime()
        time_stamp = calendar.timegm(current_GMT)
        formatted_time = datetime.fromtimestamp(time_stamp, timezone.utc).strftime('%d/%m/%Y %H:%M:%S')

        # Append new data to the existing CSV file
        if not status:
            with open(unsortedFilePath, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([user_name, character_name, health, score, "Not Completed", formatted_time])
        else:
            self.slow.slow_print("""
            Congratulations!
            You have rescued the princess and there is no one to stop you now.

            Game Completed. 

            """)
            with open(unsortedFilePath, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([user_name, character_name, health, score, "Completed", formatted_time])
        # Read the updated CSV file and sort the data
        df = pd.read_csv(unsortedFilePath)
        sorted_df = df.sort_values(by=["Score"], ascending=False)

        sorted_df.to_csv(sortedFilePath, index=False)

        data = pd.read_csv(sortedFilePath)
        data.index = data.index + 1
        print("""
        
        
        """)
        print("=" * 32 + "Leader Board" + "=" * 32)
        print()
        print(data)

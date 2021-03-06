import json, os

path_to_json = 'F:/Python_DataAnalysis_Assignments/DataAnalysisPythonRepository_001680280/MidTerm/Questions/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]


userId = []
page = 0
downvote_for_user = {}

for js in json_files:
    with open(os.path.join(path_to_json, js)) as json_file:
        data = json.load(json_file)
    users = data['items']
    for item in users:
        try:
            if item['owner']['user_id'] is not None and item['owner']['user_id'] not in userId: # Else condition for this?
                 if item['score'] < 0:
                    if item['owner']['user_id'] in downvote_for_user:
                        downvote_for_user[item['owner']['user_id']] +=  1
                    else:
                        downvote_for_user[item['owner']['user_id']] = 1

        except KeyError:
            continue

sorted_downvote = sorted(downvote_for_user.items(), key=lambda x:x[1], reverse = True)
print(sorted_downvote [:10]) # Print all the values rather than just 10.

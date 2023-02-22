import argparse

class user:
    def __init__(self, gender, age, occupation):
        self.gender = gender
        self.age = age
        self.occupation = occupation


class user_loader:
    def __init__(self):
        self.user_dict = self.load_user()
        self.gender_list, self.age_list, self.occupation_list = self.load_attribute_user()


    def load_user(self):  # map the feature entries in all files, kept in self.features dictionary
        parser = argparse.ArgumentParser(description=''' load user data''')

        parser.add_argument('--user_data_file', type=str, default='./ML100K/usersdata.txt')

        parsed_args = parser.parse_args()

        user_file = parsed_args.user_data_file
        user_dict = {}

        fr = open(user_file, 'r')
        for line in fr:
            lines = line.replace('\n', '').split('|')
            # if len(lines) != 4:
            #     continue
            user_id = lines[0]
            gender_list = []
            gender = lines[1]
            gender_list.append(int(gender))
            age_list = []
            age = int(lines[2]) // 3
            age_list.append(int(age))
            occupation_list = []
            occupation = lines[3]
            occupation_list.append(int(occupation))
            new_user = user(gender_list, age_list, occupation_list)
            user_dict[user_id]=new_user
        fr.close()
        return user_dict

    def load_attribute_user(self):  # map the feature entries in all files, kept in self.features dictionary
        parser = argparse.ArgumentParser(description=''' load user data''')

        parser.add_argument('--user_data_file', type=str, default='./ML100K/usersdata.txt')

        parsed_args = parser.parse_args()

        user_file = parsed_args.user_data_file
        gender_list = [0, 1]
        age_list = []
        occupation_list = []
        fr = open(user_file, 'r')
        for line in fr:
            lines = line.replace('\n', '').split('|')
            # if len(lines) != 4:
            #     continue
            age = int(lines[2]) // 3
            if int(age) not in age_list:
                age_list.append(int(age))
            occupation = lines[3]
            if int(occupation) not in occupation_list:
                occupation_list.append(int(occupation))
        fr.close()
        return gender_list, age_list, occupation_list




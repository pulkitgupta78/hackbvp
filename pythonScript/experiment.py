import time
import sys
import json

class Stroke:
    weights = {}
    questions = {}
    is_long_term = 0

    def __init__(self):
        self.weights = {"face": 45, "arm": 45, "speech difficulty": 45}
        self.questions = {}

    def get_keys(self):
        return self.weights.keys()

    def get_weights(self):
        return self.weights


class CardiacArrest:
    weights = {}
    questions = {}
    is_long_term = 0

    def __init__(self):
        self.weights = {"speech drop": 45, "dropped pulse": 80, "chest": 20}
        self.questions = {}

    def get_keys(self):
        return self.weights.keys()

    def get_weights(self):
        return self.weights


class HeartAttack:
    weights = {}
    questions = {}
    is_long_term = 0

    def __init__(self):
        self.weights = {"arm": 20, "sweating": 20, "chest": 35,
                        "abdomen": 20, "shoulder": 20,
                        "ingestion": 5, "vomiting": 10}
        self.questions = {}

    def get_keys(self):
        return self.weights.keys()

    def get_weights(self):
        return self.weights


class Parkinson:
    weights = {}
    questions = {}
    is_long_term = 1

    def __init__(self):
        self.weights = {"tremor": 20, "slowed": 10, "rigid": 5,
                        "balance": 15, "speech": 10,
                        "writing": 20}
        self.questions = {"Have you felt recent shaking or trembling": 20, "Having trouble writing": 30,
                          "Felt hearing impairment": 20, "Finding it hard to balance": 20, "Felt rigidity in muscles": 30}

    def conditions(self):
        # Condition for Parkinson
        return

    def get_keys(self):
        return self.weights.keys()

    def get_weights(self):
        return self.weights


class Tuberculosis:
    weights = {}
    questions = {}
    is_long_term = 1

    def __init__(self):
        self.weights = {"blood": 40, "chest": 20,
                        "weakness": 2, "coughStrengh": 3.5}
        self.questions = {"Cough for straight 21 days": 80, "Lower chest pains": 20, "Increase fatigue": 20,
                          "Blood in cough": 30, "Fatigue": 10, "Wet cough": 30}

    def get_keys(self):
        return self.weights.keys()

    def conditions(self):
        # Check from log of last 21 days.
        return

    def get_weights(self):
        return self.weights


class Diabetes:
    weights = {}
    questions = {}
    is_long_term = 1

    def __init__(self):
        self.weights = {"thirst": 2, "hunger": 2, "urine": 2, "weight": 4, "fatigue": 4, "blurred": 20}
        self.questions = {"Dry throat": 10, "Increased hunger": 10, "Frequent urination or urine infections": 20,
                          "Increased fatigue": 20, "Blurred Vision": 30}

    def get_keys(self):
        return self.weights.keys()

    def accumulative(self):
        # Diabetes Conditions. Moniter weight, and other factors.

        return

    def get_weights(self):
        return self.weights


class Diseases:
    def __init__(self, ifp, ofp):
        self.input_file_path = ifp
        self.output_file_path = ofp
        self.Stroke = Stroke()
        self.Tuberculosis = Tuberculosis()
        self.Parkinson = Parkinson()
        self.HeartAttack = HeartAttack()
        self.CardiacArrest = CardiacArrest()
        self.Diabetes = Diabetes()

    def write_in_log(self, score):
        output_file = open(self.output_file_path, "a")
        '''
        local_time = time.localtime(time.time())
        log_date_time = local_time.tm_year + " " + local_time.tm_mon + " " + local_time.tm_hour + " " + \
                        local_time.tm_min
        string_to_write = "d/t : " + log_date_time + " "
        '''

        string_to_write = "{"
        for i in score.keys():
            string_to_write += "\"" + i + "\"" + ": " + "\"" + str(score[i]) + "\", "

        string_to_write_modified = string_to_write[:-2] + "}\n"

        output_file.write(string_to_write_modified)
        output_file.close()

    def calculate_score(self, input_string):

        score = {"Stroke": 0, "HeartAttact": 0, "Parkinson": 0,
                 "Tuberculosis": 0, "CardiacArrest": 0, "Diabetes": 0}

        for i in input_string.split():
            if i in self.Stroke.weights.keys():
                score["Stroke"] += self.Stroke.weights[i]
            elif i in self.Tuberculosis.weights.keys():
                score["Tuberculosis"] += self.Tuberculosis.weights[i]
            elif i in self.CardiacArrest.weights.keys():
                score["CardiacArrest"] += self.CardiacArrest.weights[i]
            elif i in self.HeartAttack.weights.keys():
                score["HeartAttact"] += self.HeartAttack.weights[i]
            elif i in self.Parkinson.weights.keys():
                score["Parkinson"] += self.Parkinson.weights[i]
            elif i in self.Diabetes.weights.keys():
                score["Diabetes"] += self.Diabetes.weights[i]

        self.write_in_log(score)

        score_max = 0
        score_term = "None"
        for i in score.keys():
            if score[i] > score_max:
                score_max = score[i]
                score_term = i

        return score_term, score_max

    '''

    def call_questions(self, disease_code):
        if disease_code == 0:
            self.Diabetes.
        elif disease_code == 1:
        elif disease_code == 2:
    '''


    def calculateAccumulative(self):
        print "here"
        a = input()
        log = open(outputFileAddress, "r")
        accumulative_output_file = open(accumulativeOutput, "rw+")
        #accumulative_output_file.truncate(0)
        ultimate_score = {"Stroke": 0, "HeartAttact": 0, "Parkinson": 0, "Tuberculosis": 0, "CardiacArrest": 0, "Diabetes": 0}
        for i in log.readlines():
            print len(i)
            a = input()
            parsed_json = json.loads(i)
            for j in parsed_json.keys():
                ultimate_score[j] += (int)(parsed_json[j])

        string_to_write = "{"
        for i in ultimate_score.keys():
            string_to_write += "\"" + i + "\"" + ": " + "\"" + str(ultimate_score[i]) + "\", "

        string_to_write_modified = string_to_write[:-2] + "}\n"
        accumulative_output_file.write(string_to_write_modified)
        accumulative_output_file.close()

    def engage(self, input_string):
        score_term, score_max = self.calculate_score(input_string)
        self.calculateAccumulative()
        if score_max >= 70:
            print score_max, score_term


inputFileAddress = sys.argv[1]
outputFileAddress = sys.argv[2]
accumulativeOutput = sys.argv[3]
print sys.argv
inputFile = open(inputFileAddress, "r")
inputText = inputFile.read()
user1 = Diseases(inputFileAddress, outputFileAddress)
user1.engage(inputText)
inputFile.close()
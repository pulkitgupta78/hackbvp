class Diseases:
    def __init__(self, ifp, ofp):
        self.input_file_path = ifp
        self.output_file_path = ofp

    class Stroke:
        weights = {}
        questions = {}

        def __init__(self):
            self.weights = {"face": 45, "arm weakness": 45, "speech difficulty": 45}
            self.questions = {}

        def get_keys(self):
            return self.weights.keys()

        def get_weights(self):
            return self.weights

    class CardiacArrest:
        weights = {}
        questions = {}

        def __init__(self):
            self.weights = {"speech drop": 45, "Dropped Pulse": 80}
            self.questions = {}

        def get_keys(self):
            return self.weights.keys()

        def get_weights(self):
            return self.weights

    class HeartAttack:
        weights = {}
        questions = {}

        def __init__(self):
            self.weights = {"arm Pain": 20, "Sweating": 20, "Chest": 35,
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

        def __init__(self):
            self.weights = {"tremor": 20, "slowed Moment": 10, "rigid Muscles": 5,
                            "balance": 15, "speech": 10,
                            "writing": 20}
            self.questions = {}

        def get_keys(self):
            return self.weights.keys()

        def get_weights(self):
            return self.weights

    class Tuberculosis:
        weights = {}
        questions = {}

        def __init__(self):
            self.weights = {"coughing": 30, "blood": 40, "chest": 20,
                            "weakness": 2, "coughStrengh": 3.5}
            self.questions = {}

        def get_keys(self):
            return self.weights.keys()

        def get_weights(self):
            return self.weights

    def write_in_log(self, score):
        output_file = open(self.output_file_path, "w")
        for i in score.keys():
            output_file.write(i + " " + (str)(score[i]) + " ")

    def calculate_score(self, input_string):

        score = {"stroke": 0, "heartArrest": 0, "parkinson": 0,
                 "tuberculosis": 0, "cardiacArrest": 0}

        for i in input_string.split():
            if i in self.Stroke.weights.keys():
                score["stroke"] += self.Stroke.weights[i]
            elif i in self.Tuberculosis.weights.keys():
                score["tuberculosis"] += self.Tuberculosis.weights[i]
            elif i in self.CardiacArrest.weights.keys():
                score["cardiacArrest"] += self.CardiacArrest.weights[i]
            elif i in self.HeartAttack.weights.keys():
                score["heartArrest"] += self.HeartAttack.weights[i]
            elif i in self.Parkinson.weights.keys():
                score["parkinson"] += self.Parkinson.weights[i]

        a = input()

        self.write_in_log(score)

        score_max = 0
        score_term = "None"
        for i in score.keys():
            if score[i] > score_max:
                score_max = score[i]
                score_term = i

        return score_term, score_max

    def engage(self, input_string):
        score_term, score_max = self.calculate_score(input_string)
        if score_max >= 70:
            print score_max, score_term



inputFileAddress = "/home/pulkit/Desktop/logged.txt"
inputFile = open(inputFileAddress, "r")
inputText = inputFile.read()
user1 = Diseases(inputFileAddress, "/home/pulkit/Desktop/newlog.txt")
user1.engage(inputText)










# structure based off of https://github.com/chridey/cmv/blob/master/cmv/bin/cmv_predict_rnn.py
import sys
from release.lstm.SarcasmClassifier import SarcasmClassifier
from release.preprocessing.load_data import load_data
from sklearn.model_selection import train_test_split
import numpy as np
from datetime import datetime


if __name__ == "__main__":

    targets = ["one", "two", "three", "four", "five"]
    time_stamp = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    log_file = open("output/logs/log_file_{}".format(time_stamp), "w+")
    #targets = ["one"]
    targets = ["one"]
    for target in targets:
        print("working on target: {}\n".format(target))
        log_file.write("working on target: {}\n".format(target))

        #load_data(target, sys.argv[1])
        training, y, testing, test_y, kwargs = load_data(target, sys.argv[1])
        classifier = SarcasmClassifier(**kwargs)
        attention_classifier = classifier.classifier
        filename = "/Users/alexfabbri/Desktop/school/Spring2017/research/research_deep_learning_tests_spring2017/deep_learning_nlp_sarcasm/release/main/output/models/classifier_one_2017-04-05_20:24:13.npz"
        with np.load(filename) as f:
            param_values = [f['arr_%d' % i] for i in range(len(f.files))]
        attention_classifier.set_params(param_values)
        test_sentence_attention = attention_classifier.sentence_attention_response(*testing)
        test_sentence_context = attention_classifier.sentence_attention_context(*testing)
        for i in range(test_sentence_context.shape[0]):
            print("example: {} \n".format(i))
            print(test_sentence_context[i])
            print(test_sentence_attention[i])
            print("finished example: {} \n".format(i))

        #classifier.fit(training, y, log_file)
        #classifier.save('output/models/classifier_{}_{}'.format(target, time_stamp))
        #preds,scores = classifier.predict(testing, test_y)
        #precision, recall, fscore = scores[0], scores[1], scores[2]

        #log_file.write("precision for target {} : {}".format(target, precision))
        #log_file.write("recall for target {} : {}".format(target, recall))
        #log_file.write("fscore for target {} : {}".format(target, fscore))
        #log_file.flush()
        #np.save('output/preds/preds_{}_{}'.format(target, time_stamp), preds)
        #print("finished target: {}\n".format(target))

    log_file.close()        
        
#!/usr/bin/env python
from tools.load import LoadMatrix
from numpy import random
lm=LoadMatrix()

ground_truth = lm.load_labels('../data/label_train_twoclass.dat')
random.seed(17)
predicted = random.randn(len(ground_truth))

parameter_list = [[ground_truth,predicted]]

def evaluation_contingencytableevaluation (ground_truth, predicted):
	from shogun import BinaryLabels
	import shogun as sg

	ground_truth_labels = BinaryLabels(ground_truth)
	predicted_labels = BinaryLabels(predicted)

	base_evaluator = sg.evaluation("ContingencyTableEvaluation")
	base_evaluator.evaluate(predicted_labels,ground_truth_labels)

	evaluator = sg.evaluation("AccuracyMeasure")
	accuracy = evaluator.evaluate(predicted_labels,ground_truth_labels)

	evaluator = sg.evaluation("ErrorRateMeasure")
	errorrate = evaluator.evaluate(predicted_labels,ground_truth_labels)

	evaluator = sg.evaluation("BALMeasure")
	bal = evaluator.evaluate(predicted_labels,ground_truth_labels)

	evaluator = sg.evaluation("WRACCMeasure")
	wracc = evaluator.evaluate(predicted_labels,ground_truth_labels)

	evaluator = sg.evaluation("F1Measure")
	f1 = evaluator.evaluate(predicted_labels,ground_truth_labels)

	evaluator = sg.evaluation("CrossCorrelationMeasure")
	crosscorrelation = evaluator.evaluate(predicted_labels,ground_truth_labels)

	evaluator = sg.evaluation("RecallMeasure")
	recall = evaluator.evaluate(predicted_labels,ground_truth_labels)

	evaluator = sg.evaluation("PrecisionMeasure")
	precision = evaluator.evaluate(predicted_labels,ground_truth_labels)

	evaluator = sg.evaluation("SpecificityMeasure")
	specificity = evaluator.evaluate(predicted_labels,ground_truth_labels)

	return accuracy, errorrate, bal, wracc, f1, crosscorrelation, recall, precision, specificity


if __name__=='__main__':
	print('EvaluationContingencyTableEvaluation')
	evaluation_contingencytableevaluation(*parameter_list[0])


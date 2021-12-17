'''
Utilities Related to Responsible AI components: Interpretability & Fairness
'''

import pandas as pd
from interpret.ext.blackbox import TabularExplainer
from fairlearn.metrics._group_metric_set import _create_group_metric_set

def interpret_global(model, train, test, features=None, classes=None, local=False, task=None):
    # explain predictions on your local machine
    # "features" and "classes" fields are optional
    explainer = TabularExplainer(model, 
                                train,
                                features=features,
                                classes=classes,
                                model_task=task
                                )

    # explain overall model predictions (global explanation)
    global_explanation = explainer.explain_global(test)

    # uploading global model explanation data for storage or visualization in webUX
    # the explanation can then be downloaded on any compute
    # multiple explanations can be uploaded
    return global_explanation

def fairness_binary(model, model_id, sensitive_feat, X_test, y_test) :
    #  Create a dictionary of model(s) you want to assess for fairness 
    ys_pred = { model_id: model.predict(X_test)}
    dash_dict = _create_group_metric_set(y_true=y_test,
                                        predictions=ys_pred,
                                        sensitive_features=validate_for_fairness(sensitive_feat, y_test),
                                        prediction_type='binary_classification')

    return dash_dict

def fairness_regression(model, model_id, sensitive_feat, X_test, y_test) :
    #  Create a dictionary of model(s) you want to assess for fairness 
    ys_pred = { model_id: model.predict(X_test).reshape(-1,1)}
    dash_dict = _create_group_metric_set(y_true=y_test,
                                        predictions=ys_pred,
                                        sensitive_features=sensitive_feat,
                                        prediction_type='regression')

    return dash_dict

def fairness_multiclass(model, model_id, sensitive_feat, X_test, y_test) :
    #TODO: Adding MultiClass Support to Fairlearn requires open source modifications / extensive, see if use case. 
    # For now workaround is regression

    return fairness_regression(model, model_id, sensitive_feat, X_test, y_test)


def validate_for_fairness(sensitive_feat, y_test):
    sensitive_test_data = pd.concat([y_test, sensitive_feat], axis=1)

    label_column = y_test.columns[0]
    resolved = sensitive_test_data.groupby([label_column]).nunique()

    excluded_set = set()
    for label_value, row in resolved.iterrows():
        for feature_name, r in row.iteritems():
            if r < 2:
                print(f"Feature {feature_name} had less than 2 unique values ({r}) for Ground Truth Label {label_value} - Excluding column from fairness evaluation")
                excluded_set.add(feature_name)

    print(f"Final exclusion list: {excluded_set}")
    new_sens = sensitive_feat.drop(columns=list(excluded_set))
    return new_sens

def save_ebm_explanations(ebm):
    import os
    os.mkdir("images")

    ebm_global= ebm.explain_global()
    for index, value in enumerate(ebm.feature_groups_):
        plotly_fig = ebm_global.visualize(index)
        plotly_fig.write_image(f"images/fig_{index}.png")

    return True



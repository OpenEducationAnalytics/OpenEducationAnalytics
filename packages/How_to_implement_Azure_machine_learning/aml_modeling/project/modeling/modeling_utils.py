from typing import List, Tuple

import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd

from sklearn.metrics import precision_recall_fscore_support, accuracy_score
from sklearn.metrics import roc_auc_score

from .OEA_model import OEAModelInterface, ModelType, ExplanationType

def log_metrics(model, dataset="training"):

    if dataset == "training_val":
        X_train_val = pd.concat([model.X_train, model.X_val], axis=0)
        y_train_val = np.concatenate([model.y_train, model.y_val], axis=0)
        x = X_train_val
        y_true = y_train_val

    elif dataset == "training":
        x = model.X_train
        y_true = model.y_train

    elif dataset == "test":
        x = model.X_test
        y_true = model.y_test

    else:
        raise ValueError("Dataset to log must be training, training_val, or test")

    score = model.predictor.score(x, y_true)
    mlflow.log_metric(f"{dataset}_score", score)

    preds = model.predictor.predict(x)
    if model.model_type == ModelType.binary_classification:
        precision, recall, f, _ = precision_recall_fscore_support(y_true, preds, average="binary")
    elif model.model_type == ModelType.multiclass_classification:
        precision, recall, f, _ = precision_recall_fscore_support(y_true, preds, average="macro")
    
    if model.model_type == ModelType.regression:
        ##Add Specific metrics to regression models here
        return preds
    else:
        preds_prob = model.predictor.predict_proba(x)[:, 1]
        score_auc = roc_auc_score(y_true, preds_prob)

        mlflow.log_metric(f"{dataset}_auc", score_auc)
        mlflow.log_metric(f"{dataset}_precision_score", precision)
        mlflow.log_metric(f"{dataset}_recall_score", recall)
        mlflow.log_metric(f"{dataset}_f1_score", f)

    return preds
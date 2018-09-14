# flake8: noqa

# Registry keys

BACKEND = 'BACKEND'

## Backend Keys

TF_OBJECT_DETECTION = 'TF_OBJECT_DETECTION'
KERAS_CLASSIFICATION = 'KERAS_CLASSIFICATION'
TF_DEEPLAB = 'TF_DEEPLAB'

## Model keys

### TF Object Detection
SSD_MOBILENET_V1_COCO = 'SSD_MOBILENET_V1_COCO'

## Keras Classificaiton
RESNET50_IMAGENET = 'RESNET50_IMAGENET'

## XCEPTION_65
XCEPTION_65 = 'XCEPTION_65'

from .backend_config import BackendConfig
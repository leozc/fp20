# Merge into Pants Build

NOTE: this example folder is copied directly from [pytorch-lightning|<https://github.com/PyTorchLightning/pytorch-lightning/blob/master/pl_examples>].

The follow operation were done to merge into the Pants System

* Add `pytorch_lightning>=1.2.8` and `torchvision>=0.9.1`

* Generate constraints `build-support/generate_constraints.sh`

* Run `./pants tailor pl_examples:`

* Done!

# Examples
Our most robust examples showing all sorts of implementations
can be found in our sister library [lightning-bolts](https://lightning-bolts.readthedocs.io/en/latest/convolutional.html#gpt-2).

---

## Basic examples
In this folder we add 3 simple examples:

* [MNIST Classifier](https://github.com/PyTorchLightning/pytorch-lightning/blob/master/pl_examples/basic_examples/simple_image_classifier.py) (defines the model inside the `LightningModule`).
* [Image Classifier](https://github.com/PyTorchLightning/pytorch-lightning/blob/master/pl_examples/basic_examples/backbone_image_classifier.py) (trains arbitrary datasets with arbitrary backbones).
* [Autoencoder](https://github.com/PyTorchLightning/pytorch-lightning/blob/master/pl_examples/basic_examples/autoencoder.py) (shows how the `LightningModule` can be used as a system)

---

## Domain examples
This folder contains older examples. You should instead use the examples
in [lightning-bolts](https://lightning-bolts.readthedocs.io/en/latest/convolutional.html#gpt-2)
for advanced use cases.

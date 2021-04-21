# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import importlib
import platform
from unittest import mock

import pytest
import torch

from pl_examples import _DALI_AVAILABLE

ARGS_DEFAULT = """
--trainer.default_root_dir %(tmpdir)s \
--trainer.max_epochs 1 \
--trainer.limit_train_batches 2 \
--trainer.limit_val_batches 2 \
--data.batch_size 32 \
"""

ARGS_GPU = ARGS_DEFAULT + """
--trainer.gpus 1 \
"""

ARGS_DP = ARGS_DEFAULT + """
--trainer.gpus 2 \
--trainer.accelerator dp \
"""

ARGS_AMP = """
--trainer.precision 16 \
"""


@pytest.mark.parametrize(
    'import_cli', [
        'pl_examples.basic_examples.simple_image_classifier',
        'pl_examples.basic_examples.backbone_image_classifier',
        'pl_examples.basic_examples.autoencoder',
    ]
)
@pytest.mark.skipif(torch.cuda.device_count() < 2, reason="test requires multi-GPU machine")
@pytest.mark.parametrize('cli_args', [ARGS_DP, ARGS_DP + ARGS_AMP])
def test_examples_dp(tmpdir, import_cli, cli_args):

    module = importlib.import_module(import_cli)
    # update the temp dir
    cli_args = cli_args % {'tmpdir': tmpdir}

    with mock.patch("argparse._sys.argv", ["any.py"] + cli_args.strip().split()):
        module.cli_main()


@pytest.mark.parametrize(
    'import_cli', [
        'pl_examples.basic_examples.simple_image_classifier',
        'pl_examples.basic_examples.backbone_image_classifier',
        'pl_examples.basic_examples.autoencoder',
    ]
)
@pytest.mark.parametrize('cli_args', [ARGS_DEFAULT])
def test_examples_cpu(tmpdir, import_cli, cli_args):

    module = importlib.import_module(import_cli)
    # update the temp dir
    cli_args = cli_args % {'tmpdir': tmpdir}

    with mock.patch("argparse._sys.argv", ["any.py"] + cli_args.strip().split()):
        module.cli_main()


@pytest.mark.skipif(not _DALI_AVAILABLE, reason="Nvidia DALI required")
@pytest.mark.skipif(not torch.cuda.is_available(), reason="test requires GPU machine")
@pytest.mark.skipif(platform.system() != 'Linux', reason='Only applies to Linux platform.')
@pytest.mark.parametrize('cli_args', [ARGS_GPU])
def test_examples_mnist_dali(tmpdir, cli_args):
    from pl_examples.basic_examples.dali_image_classifier import cli_main

    # update the temp dir
    cli_args = cli_args % {'tmpdir': tmpdir}
    with mock.patch("argparse._sys.argv", ["any.py"] + cli_args.strip().split()):
        cli_main()

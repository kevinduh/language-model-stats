Organisation | Model | Citation | Architecture | Data | Tokens (B) | Size (B) | Compute | Training Strategy
---|---|---|---|---|---|---|---|---
Google | Mbert | [Devlin 2019](https://github.com/google-research/bert/blob/master/multilingual.md) | EncDec | Wikipedia | ? | 0.1 | ? | MLM, Next Sentence Prediction
Meta | MBART-large | [Liu 2020](https://arxiv.org/pdf/2001.08210.pdf) | Enc-Dec | CC25, backtranslate | ? | 0.6 | 256 Nvidia V100 GPUs for 18 days | MLM; (Bart training), sentence shuffling
Meta | XGLM | [Lin 2021](https://arxiv.org/pdf/2112.10668.pdf) | EncDec | CC100 | 500 | 7.5 | v100s for ? | AR; Trained on mixture of monoligual texts
Meta | XLMR | [Goyal 2020](https://arxiv.org/pdf/1911.02116.pdf) | Enc-Dec | CC100 | 167 | 10.7 |  | MLM
Google | Byt5 | [Xue 2022](https://arxiv.org/pdf/2105.13626.pdf) | Enc-Dec | MC4 | 6.4T | 12.9 | ? | Token free (byte level MT5)
Google | MT5 | [Xue 2021](https://arxiv.org/pdf/2010.11934.pdf) | Enc-Dec | MC4 | 6.4T | 13 | ? | MLM
Meta | M2M100 | [Fan 2020](https://arxiv.org/pdf/2010.11125.pdf) | Enc-Dec | CCMatrix, backtranslate | 7.5 parallel sentences; | 15.4 | "hundreds of GPUs" | AR


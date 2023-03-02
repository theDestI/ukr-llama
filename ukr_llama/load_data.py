from datasets import load_dataset

load_dataset('wikipedia', '20230220.uk', beam_runner='DirectRunner', cache_dir='data')
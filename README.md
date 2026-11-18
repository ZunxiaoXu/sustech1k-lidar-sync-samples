# SUSTech1K synchronized LiDAR samples

This package contains 100 randomly selected nonempty synchronized LiDAR sequences from SUSTech1K, exported on 2026-11-18. The modality is `08-sync-*-LiDAR-PCDs.pkl`.

Sampling uses seed 20261118 and the existing full sequence index of 25,239 SUSTech1K sequences. Candidate paths are sorted, shuffled, and read in order until 100 nonempty sequences have been collected. The manifest records the selected sequences and any skipped empty sequences.

The archive preserves the identity, condition and view directory hierarchy under `SUSTech1K/`. Each pickle file contains a list of frames. Each frame is a NumPy array of XYZ points with shape `(number_of_points, 3)`. Frame point counts vary. These are the official synchronized LiDAR frames at nominal 10 Hz.

All sampled pickle bytes are preserved. `sample_manifest.json` records the SHA256, size, frame count and point counts of every sequence. `sample_index.csv` provides a compact file list.

Install NumPy in the analysis environment, then run the reader on the downloaded ZIP.

```sh
python -m pip install numpy
python read_lidar.py SUSTech1K_08-sync_random100_20261118.zip
```

Use `--member` to select a sequence by its archive path and `--frame` to select a zero-based frame index.

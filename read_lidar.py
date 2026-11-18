"""Read a synchronized LiDAR sequence from the sample archive."""
import argparse
import pickle
import zipfile


def read_sequence(archive_path, member=None):
    with zipfile.ZipFile(archive_path) as archive:
        if member is None:
            member = next(name for name in archive.namelist() if name.endswith(".pkl"))
        with archive.open(member) as source:
            return member, pickle.load(source)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive")
    parser.add_argument("--member")
    parser.add_argument("--frame", type=int, default=0)
    arguments = parser.parse_args()
    member, sequence = read_sequence(arguments.archive, arguments.member)
    frame = sequence[arguments.frame]
    print("Sequence", member)
    print("Frames", len(sequence))
    print("Frame index", arguments.frame)
    print("Point array shape", frame.shape)
    print("Data type", frame.dtype)
    print("First four XYZ points", frame[:4])

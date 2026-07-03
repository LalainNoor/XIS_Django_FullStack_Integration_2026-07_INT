import cv2
from pathlib import Path

from inference.services.inference_engine import InferenceEngine


def main():

    engine = InferenceEngine()

    print("=" * 60)
    print("MODEL INFORMATION")
    print("=" * 60)
    print(engine.get_model_info())

    input_dir = Path("../input")

    print("\n")
    print("=" * 60)
    print("RUNNING TESTS")
    print("=" * 60)

    for image_path in sorted(input_dir.glob("*.jpg")):

        image = cv2.imread(str(image_path))

        if image is None:
            print(f"Failed to load {image_path.name}")
            continue

        result = engine.predict(image)

        print(f"{image_path.name:15} -> "
              f"{result['prediction']:10} "
              f"({result['confidence']}%)")


if __name__ == "__main__":
    main()
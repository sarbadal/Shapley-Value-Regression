import argparse

from shapley import ShapleyValue
from shapley.data.load import get_available_datasets, get_dataset_info, load_dataset


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Shapley value regression on a packaged dataset")
    parser.add_argument(
        "--dataset",
        default="death_rate",
        choices=get_available_datasets(),
        help="Dataset key to use",
    )
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    dataset_info = get_dataset_info(args.dataset)

    print(f"Dataset: {dataset_info['name']}")
    print(f"Description: {dataset_info['description']}")
    print(f"Default X: {dataset_info['default_X']}")
    print(f"Target: {dataset_info['target']}")

    df = load_dataset(args.dataset)
    features = dataset_info["default_X"]
    target = dataset_info["target"]

    sv = ShapleyValue(df, features, target)
    # contribution_all = sv.get_shapley_contribution(verbose=False)
    focus_x_contribution, _ = sv.get_shapley_contribution_of(target_x="Distance_Metro_KM", verbose=False)
    # print(contribution_all)
    print(f"Contribution of 'Distance_Metro_KM': {focus_x_contribution}")


if __name__ == "__main__":
    # python3 main.py
    # python3 -B main.py --dataset distance_metro
    # python3 -B main.py --dataset death_rate
    main()
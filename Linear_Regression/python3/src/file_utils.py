from pathlib import Path
from data_logger import DataLogger
import pandas as pd
from matplotlib import figure as fig


_dlog           : DataLogger    = DataLogger()
_data_dir_path  : Path          = (Path(__file__).parent.parent.parent / "dat").resolve()
_plot_dir_path  : Path          = (Path(__file__).parent.parent.parent / "plt").resolve()


def _createDirIfNotExists(p: Path) -> None:
    """
    Checks whether the given directory exists. If not, it creates it.

    Args:
        p : Target directory path.
    """
    if not p.exists():
        p.mkdir(parents = True, exist_ok = True)


def checkXYColumns(df: pd.DataFrame) -> None:
    """
    Checks whether expected columns (X and Y) are included in the DataFrame object. 
    Raises an exception if such condition is not met.
    
    Args:
        df              : Input Pandas DataFrame object.
    """

    if "X" not in df.columns or "Y" not in df.columns:
        raise ValueError("Column names do not match (\"X\", \"Y\")")
    
    if len(df.columns) > 2:
        raise ValueError(f"Found more columns than expected ({df.columns})")


def saveDataAsCSV(df: pd.DataFrame, save_csv_name: str) -> None:
    """
    Save data (provided as Pandas DataFrame object) in a csv file. 

    Args:
        df              : Input Pandas DataFrame object.
        save_csv_path   : Target output csv file name.
    """

    _dlog.logInf("Saving DataFrame object as .csv file...")

    _createDirIfNotExists(_data_dir_path)

    data_file_path: Path = _data_dir_path / save_csv_name

    df.to_csv(data_file_path, index = False)

    _dlog.logInf(f"Saved DataFrame as {str(data_file_path)}.")


def loadDataFromCSV(data_file_name: str) -> pd.DataFrame:
    """
    Loads data from a CSV file.

    Args:
        data_file_name : Target directory path.
    
    Returns:
        A Pandas DataFrame object.
    """
    if not _data_dir_path.exists():
        raise NotADirectoryError(f"Could not find hosting directory: {str(_data_dir_path)}.")

    file_path: Path = _data_dir_path / data_file_name

    if not file_path.exists():
        raise FileNotFoundError(f"Could not find specified file: {str(file_path)}.")
    
    _dlog.logInf(f"Returning Pandas DataFrame object from file in: {str(file_path)}.")

    return pd.read_csv(file_path)


def savePlotAsPNG(target_fig: fig, plot_file_name: str) -> None:
    """
    Saves given plot.

    Args:
        target_fig      : Figure to be saved.
        plot_file_name  : Target file name.
    """
    _createDirIfNotExists(_plot_dir_path)

    plot_path: Path = _plot_dir_path / plot_file_name

    target_fig.savefig(plot_path)
    _dlog.logInf(f"Saved data plot as {str(Path(plot_path).resolve())}.")

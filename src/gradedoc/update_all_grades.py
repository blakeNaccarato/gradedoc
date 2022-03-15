"""Update all grades."""

from __future__ import annotations

from typing import Optional

import docxrev

from gradedoc import shared
from gradedoc.shared import Path
from gradedoc.update_grade import update_grade


def update_all_grades(
    directory: Optional[Path] = None, gradebook_path: Optional[Path] = None
):
    """Update all grades.

    Update all grades from all documents in `directory` as specified in
    :py:func:`shared.get_paths`.

    Parameters
    ----------
    directory
        The directory containing the documents.
    gradebook_name
        The name of the gradebook (include ".csv"). Defaults to "grades.csv".
    """

    (paths, gradebook_path) = shared.get_paths(directory)

    for path in paths:
        document = docxrev.Document(path)
        update_grade(document, gradebook_path)

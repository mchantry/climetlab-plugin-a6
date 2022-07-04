#!/usr/bin/env python3# (C) Copyright 2021 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#
from .abc import Weather


class ModelLevelWeather(Weather):
    """Weather data for the model levels."""

    name = "Weather data for specific model levels"
    documentation = (
        "Contains weather data for whole Europe. The variables are "
        "provided for different model levels (see "
        "https://ecmwf.int/en/forecasts/documentation-and-support/137-model-levels)."
    )

    @property
    def type(self) -> str:
        """Return the weather data type."""
        return "ml"

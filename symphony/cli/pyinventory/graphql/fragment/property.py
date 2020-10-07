#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from dataclasses import dataclass
from datetime import datetime
from gql.gql.datetime_utils import DATETIME_FIELD
from gql.gql.graphql_client import GraphqlClient
from gql.gql.client import OperationException
from gql.gql.reporter import FailedOperationException
from functools import partial
from numbers import Number
from typing import Any, Callable, List, Mapping, Optional
from time import perf_counter
from dataclasses_json import DataClassJsonMixin

from ..fragment.property_type import PropertyTypeFragment, QUERY as PropertyTypeFragmentQuery
QUERY: List[str] = PropertyTypeFragmentQuery + ["""
fragment PropertyFragment on Property {
  id
  propertyType {
    ...PropertyTypeFragment
  }
  stringValue
  intValue
  floatValue
  booleanValue
  latitudeValue
  longitudeValue
  rangeFromValue
  rangeToValue
}

"""]

@dataclass
class PropertyFragment(DataClassJsonMixin):
    @dataclass
    class PropertyType(PropertyTypeFragment):
        pass

    id: str
    propertyType: PropertyType
    stringValue: Optional[str]
    intValue: Optional[int]
    floatValue: Optional[Number]
    booleanValue: Optional[bool]
    latitudeValue: Optional[Number]
    longitudeValue: Optional[Number]
    rangeFromValue: Optional[Number]
    rangeToValue: Optional[Number]
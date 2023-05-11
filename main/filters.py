from rangefilter.filters import DateRangeFilter


def date_range_filter_builder(title=None, default_start=None, default_end=None):
    """Filter date"""
    filter_cls = type(
        str("DateRangeFilter"),
        (DateRangeFilter,),
        {
            "__from_builder": True,
            "default_title": title,
            "default_start": default_start,
            "default_end": default_end,
        },
    )
    return filter_cls

from sqlalchemy import asc, desc


class BaseRepository:

    @staticmethod
    def paginate(query, start: int, end: int, page: bool):
        if page:
            query = query.limit(end).offset(start * end)
        else:
            query = query.limit(end - start).offset(start)
        return query

    @staticmethod
    def apply_sort(query, sort_arg: str, sortable: dict):
        sort_arr = sort_arg.split(',')
        for sort in sort_arr:
            sort_parsed = sort.split(' ')
            column = sort_parsed[0]
            try:
                sort_type = sort_parsed[1]
            except IndexError:
                sort_type = 'asc'

            if sort_type == 'asc':
                query = query.order_by(asc(sortable[column]))
            elif sort_type == 'desc':
                query = query.order_by(desc(sortable[column]))
        return query

    @staticmethod
    def filter(query, filter_args: tuple, filterable: dict):
        return query.where(filterable[filter_args[0]].ilike('%' + filter_args[1] + '%'))
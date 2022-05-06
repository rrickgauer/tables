from __future__ import annotations
from tables.domain.maps import DatabaseDumpMap
from tables.domain.models import TableDump
from tables.utilities import prettytables
import prettytable as pt


class ViewCommand:

    def __init__(self, database_data: DatabaseDumpMap, columns: list[str], sort: str=None):
        self._database_data = database_data
        self._columns = columns
        self._sort = sort


    def get_table(self) -> str:
        """Get table output."""

        output = ''
        for table_dump in self._database_data.values():
            prettytable = self._get_prettytable(table_dump)
            output += self._format_prettytable_output(prettytable, table_dump)

        return output

    def get_markdown(self) -> str:
        """Get markdown output."""

        output = ''
        for table_dump in self._database_data.values():
            prettytable = self._get_prettytable(table_dump)
            prettytable.set_style(pt.MARKDOWN)
            output += self._format_prettytable_output(prettytable, table_dump)

        return output

    
    def get_html(self) -> str:
        """Get html output."""

        output = ''
        for table_dump in self._database_data.values():
            prettytable = self._get_prettytable(table_dump)
                        
            output += f'{table_dump.table_name} [{table_dump.table_type.value}]\n'        # table name
            output += prettytable.get_html_string(fields=self._columns)                     # columns
            output += "\n" * 3

        return output


    def get_json(self) -> str:
        """Get json output."""
        return prettytables.dump_json(list(self._database_data.values()))

    def _get_prettytable(self, table_dump: TableDump) -> pt.PrettyTable:
        return prettytables.dataclasses_to_prettytable(table_dump.columns)


    def _format_prettytable_output(self, prettytable: pt.PrettyTable, table_dump: TableDump) -> str:
            output = ''
            output += f'{table_dump.table_name} [{table_dump.table_type.value}]\n\n'    # table name
            output += prettytable.get_string(fields=self._columns)                      # columns
            output += "\n" * 3

            return output
    
        
from langchain.tools import StructuredTool
from pydantic.v1 import BaseModel


def write_report(file_name, html):
    with open(file_name, "w") as f:
        f.write(html)


class WriteReportArgsSchema(BaseModel):
    file_name: str
    html: str


write_report_tool = StructuredTool.from_function(
    name="write_report",
    description="Write an HTML file to disk. Use this tool whenever someone asks for a report.",
    func=write_report,
    args_schema=WriteReportArgsSchema
)

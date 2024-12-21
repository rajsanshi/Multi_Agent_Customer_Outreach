from crewai_tools import DirectoryReadTool, \
                         FileReadTool, \
                         SerperDevTool
                         
directory_read_tool = DirectoryReadTool(directory='./instructions')
file_read_tool = FileReadTool()
search_tool = SerperDevTool()
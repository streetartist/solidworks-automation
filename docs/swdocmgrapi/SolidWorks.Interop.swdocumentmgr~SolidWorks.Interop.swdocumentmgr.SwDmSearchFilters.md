# SwDmSearchFilters Enumeration

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmSearchFilters`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmSearchFilters.html) on this topic. |
| SwDmSearchFilters Enumeration | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All  Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) : SwDmSearchFilters Enumeration |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Search filters. Bitmask.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Public Enum SwDmSearchFilters     Inherits System.Enum ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As SwDmSearchFilters ``` | |

| C# |  |
| --- | --- |
| ``` public enum SwDmSearchFilters : System.Enum ``` | |

| C++/CLI |  |
| --- | --- |
| ``` public enum class SwDmSearchFilters : public System.Enum ``` | |

# Members

| Member | Description |
| --- | --- |
| **SwDmSearchExternalReference** | 16 = Search for simple assembly references to parts and subassemblies |
| **SwDmSearchForAssembly** | 8 = Search for assemblies |
| **SwDmSearchForDrawing** | 4 = Search for drawings |
| **SwDmSearchForPart** | 2 = Search for parts |
| **SwDmSearchInContextReference** | 32 = Search for references to base parts for derived parts, mirrored parts, derived component parts, and parts designed in the context of assemblies |
| **SwDmSearchPartToBaseAssemblyReference** | 128 = Search for references to assemblies that have been inserted into parts using the Insert Assembly feature |
| **SwDmSearchRootAssemblyFolder** | 64 = Search all the way to the assembly's root folder |
| **SwDmSearchSubfolders** | 1 = Recursively search all of the subfolders. This is only applicable when used with [ISwDMDocument::WhereUsed](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~WhereUsed.md) and [ISwDMComponent4::GetDocument2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent4~GetDocument2.md) |

# See Also

#### 

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md)

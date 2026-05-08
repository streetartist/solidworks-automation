# SwDmBodyError Enumeration

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmBodyError`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmBodyError.html) on this topic. |
| SwDmBodyError Enumeration | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All  Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) : SwDmBodyError Enumeration |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Body errors.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Public Enum SwDmBodyError     Inherits System.Enum ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As SwDmBodyError ``` | |

| C# |  |
| --- | --- |
| ``` public enum SwDmBodyError : System.Enum ``` | |

| C++/CLI |  |
| --- | --- |
| ``` public enum class SwDmBodyError : public System.Enum ``` | |

# Members

| Member | Description |
| --- | --- |
| **swBodyErrorDecompression** | 16 = Decompression error |
| **swBodyErrorFileCreation** | 8 = Failed to create output/intermediate files |
| **swBodyErrorNoData** | 4 = Body data not present |
| **swDmBodyErrorGetCountNotCalled** | 1 = Before calling [ISwDMConfiguration::GetBody](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetBody.md), call [ISwDMConfiguration::GetBodiesCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetBodiesCount.md) |
| **swDmBodyErrorInvalidStorage** | 2 = Invalid storage |
| **swDmBodyErrorNone** | 0 = Success |

# See Also

#### 

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md)

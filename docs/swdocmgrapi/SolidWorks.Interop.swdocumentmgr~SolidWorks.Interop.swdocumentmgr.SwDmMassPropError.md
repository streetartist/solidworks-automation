# SwDmMassPropError Enumeration

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmMassPropError`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmMassPropError.html) on this topic. |
| SwDmMassPropError Enumeration | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All  Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) : SwDmMassPropError Enumeration |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Mass property errors.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Public Enum SwDmMassPropError     Inherits System.Enum ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As SwDmMassPropError ``` | |

| C# |  |
| --- | --- |
| ``` public enum SwDmMassPropError : System.Enum ``` | |

| C++/CLI |  |
| --- | --- |
| ``` public enum class SwDmMassPropError : public System.Enum ``` | |

# Members

| Member | Description |
| --- | --- |
| **swDmMassPropErrorEarlierVersion** | 1 = Mass properties are stored as document properties in version 2500 and later |
| **swDmMassPropErrorNoData** | 2 = Reason for error could be that mass properties were not calculated before the part was saved |
| **swDmMassPropErrorNone** | 0 = Success |
| **swDmMassPropErrorUnknown** | 3 = Unknown error |

# See Also

#### 

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md)

# SwDmDocumentSaveError Enumeration

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentSaveError`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentSaveError.html) on this topic. |
| SwDmDocumentSaveError Enumeration | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All  Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) : SwDmDocumentSaveError Enumeration |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Document save errors.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Public Enum SwDmDocumentSaveError     Inherits System.Enum ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As SwDmDocumentSaveError ``` | |

| C# |  |
| --- | --- |
| ``` public enum SwDmDocumentSaveError : System.Enum ``` | |

| C++/CLI |  |
| --- | --- |
| ``` public enum class SwDmDocumentSaveError : public System.Enum ``` | |

# Members

| Member | Description |
| --- | --- |
| **swDmDocumentSaveErrorFail** | 2 = Failed; reason could be related to permissions |
| **swDmDocumentSaveErrorNone** | 0 = Saved successfully |
| **swDmDocumentSaveErrorReadOnly** | 1 = Failed; file was opened as read-only |

# See Also

#### 

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md)

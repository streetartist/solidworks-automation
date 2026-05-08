# SwDmDocumentOpenError Enumeration

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentOpenError`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmDocumentOpenError.html) on this topic. |
| SwDmDocumentOpenError Enumeration | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All  Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) : SwDmDocumentOpenError Enumeration |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Document open errors.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Public Enum SwDmDocumentOpenError     Inherits System.Enum ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As SwDmDocumentOpenError ``` | |

| C# |  |
| --- | --- |
| ``` public enum SwDmDocumentOpenError : System.Enum ``` | |

| C++/CLI |  |
| --- | --- |
| ``` public enum class SwDmDocumentOpenError : public System.Enum ``` | |

# Members

| Member | Description |
| --- | --- |
| **swDmDocumentOpenErrorFail** | 1 = File failed to open; reasons could be related to permissions or the file is in use by some other application or the file does not exist |
| **swDmDocumentOpenErrorFileNotFound** | 3 = File not found |
| **swDmDocumentOpenErrorFileReadOnly** | 4 = File is read only |
| **swDmDocumentOpenErrorFutureVersion** | 6 = File was created in a version of SOLIDWORKS more recent than the SOLIDWORKS Document Manager version attempting to open the file; you need to install a later version of SOLIDWORKS Document Manager; see [ISwDMApplication::GetLatestSupportedFileVersion](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~GetLatestSupportedFileVersion.md) |
| **swDmDocumentOpenErrorNoLicense** | 5 = No valid SOLIDWORKS Document Manager API license; the file may have been saved in a later version of SOLIDWORKS to which your license key does not allow access; see **License Key** section of [Getting Started](GettingStarted-swdocmgrapi.md) |
| **swDmDocumentOpenErrorNone** | 0 = File successfully opened |
| **swDmDocumentOpenErrorNonSW** | 2 = Non-SOLIDWORKS file was opened |

# See Also

#### 

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md)

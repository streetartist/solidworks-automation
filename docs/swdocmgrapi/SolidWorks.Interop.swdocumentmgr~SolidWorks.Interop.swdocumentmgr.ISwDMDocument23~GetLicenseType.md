# GetLicenseType Method (ISwDMDocument23)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument23~GetLicenseType`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument23~GetLicenseType.html) on this topic. |
| GetLicenseType Method (ISwDMDocument23) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument23 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument23.md) : GetLicenseType Method (ISwDMDocument23) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the license type of this document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetLicenseType() As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument23 Dim value As System.Integer   value = instance.GetLicenseType() ``` | |

| C# |  |
| --- | --- |
| ``` System.int GetLicenseType() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.int GetLicenseType(); ``` | |

#### Return Value

Document Manager license type as defined in [swDMDocumentLicenseType\_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDMDocumentLicenseType_e.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument23::GetLicenseType](swdocumentmgr~SwDMDocument23~GetLicenseType.md).

# Example

See the [ISwDMDocument23](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument23.md) examples.

# See Also

#### 

[ISwDMDocument23 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument23.md)
  
[ISwDMDocument23 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument23_members.md)

# Availability

SOLIDWORKS Document Manager API 2019 SP0

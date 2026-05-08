# GetActiveSheetName Method (ISwDMDocument4)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4~GetActiveSheetName`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4~GetActiveSheetName.html) on this topic. |
| GetActiveSheetName Method (ISwDMDocument4) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4.md) : GetActiveSheetName Method (ISwDMDocument4) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the name of the active sheet in a SOLIDWORKS drawing document.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetActiveSheetName() As System.String ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument4 Dim value As System.String   value = instance.GetActiveSheetName() ``` | |

| C# |  |
| --- | --- |
| ``` System.string GetActiveSheetName() ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.String^ GetActiveSheetName(); ``` | |

#### Return Value

Name of the active sheet

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument4::GetActiveSheetName](swdocumentmgr~SwDMDocument4~GetActiveSheetName.md).

# Remarks

This method supports SOLIDWORKS drawing documents only. A -1 or NULL is returned for all other types of SOLIDWORKS documents.

# See Also

#### 

[ISwDMDocument4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4.md)
  
[ISwDMDocument4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4_members.md)
  
[ISwDMDocument4::GetSheetCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4~GetSheetCount.md)
  
[ISwDMDocument6::GetSheetNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6~GetSheetNames.md)
  
[ISwDMDocument13::GetSheetFormatPath Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetFormatPath.md)
  
[ISwDMDocument13::GetSheetProperties Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetSheetProperties.md)

# Availability

SOLIDWORKS Document Manager API 2005 FCS

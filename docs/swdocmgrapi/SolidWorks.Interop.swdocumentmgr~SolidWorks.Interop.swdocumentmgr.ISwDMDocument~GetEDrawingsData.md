# GetEDrawingsData Method (ISwDMDocument)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetEDrawingsData`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetEDrawingsData.html) on this topic. |
| GetEDrawingsData Method (ISwDMDocument) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md) : GetEDrawingsData Method (ISwDMDocument) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*eModelFileName*
:   Filename of eDrawings file to which to save the data

Obsolete as of SOLIDWORKS Document Manager API 2005 FCS. Not superseded.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetEDrawingsData( _    ByVal eModelFileName As System.String _ ) As SwDmEDwgDataError ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDocument Dim eModelFileName As System.String Dim value As SwDmEDwgDataError   value = instance.GetEDrawingsData(eModelFileName) ``` | |

| C# |  |
| --- | --- |
| ``` SwDmEDwgDataError GetEDrawingsData(     System.string eModelFileName ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDmEDwgDataError GetEDrawingsData(  &   System.String^ eModelFileName ) ``` | |

#### Parameters

*eModelFileName*
:   Filename of eDrawings file to which to save the data

#### Return Value

Success or error code as defined by [SwDmEDwgDataError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmEDwgDataError.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMDocument::GetEDrawingsData](swdocumentmgr~SwDMDocument~GetEDrawingsData.md).

 

# See Also

#### 

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.md)
  
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.md)

# Availability

SOLIDWORKS Document Manager API 2004 FCS

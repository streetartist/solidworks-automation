# Hidden Property (ISwDMTable4)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4~Hidden`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4~Hidden.html) on this topic. |
| Hidden Property (ISwDMTable4) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMTable4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4.md) : Hidden Property (ISwDMTable4) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets whether the bill of materials (BOM) table is hidden.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property Hidden As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMTable4 Dim value As System.Boolean   value = instance.Hidden ``` | |

| C# |  |
| --- | --- |
| ``` System.bool Hidden {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.bool Hidden {    System.bool get(); } ``` | |

#### Property Value

True if the BOM table is hidden, false if the BOM table is shown

# Visual Basic for Applications (VBA) Syntax

See [SwDMTable4::Hidden](swdocumentmgr~SwDMTable4~Hidden.md).

# Example

[Get BOM Tables (C#)](Get_BOM_Tables_Example_CSharp.htm)
  
[Get BOM Tables (VB.NET)](Get_BOM_Tables_Example_VBNET.htm)

# Remarks

This property only supports model documents saved in SOLIDWORKS 2012 and later.

# See Also

#### 

[ISwDMTable4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4.md)
  
[ISwDMTable4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4_members.md)

# Availability

SOLIDWORKS Document Manager API 2012 SP0

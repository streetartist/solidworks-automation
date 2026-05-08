# PartConfigurationGrouping Property (ISwDMTable4)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4~PartConfigurationGrouping`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4~PartConfigurationGrouping.html) on this topic. |
| PartConfigurationGrouping Property (ISwDMTable4) | |
| [See Also](#seealsobookmark)  [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMTable4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4.md) : PartConfigurationGrouping Property (ISwDMTable4) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the part configuration grouping for the bill of materials (BOM) table.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property PartConfigurationGrouping As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMTable4 Dim value As System.Integer   value = instance.PartConfigurationGrouping ``` | |

| C# |  |
| --- | --- |
| ``` System.int PartConfigurationGrouping {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.int PartConfigurationGrouping {    System.int get(); } ``` | |

#### Property Value

Part configuration grouping as defined in [swDMPartConfigurationGrouping](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDMPartConfigurationGrouping.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMTable4::PartConfigurationGrouping](swdocumentmgr~SwDMTable4~PartConfigurationGrouping.md).

# Example

[Get BOM Tables (C#)](Get_BOM_Tables_Example_CSharp.htm)
  
[Get BOM Tables (VB.NET)](Get_BOM_Tables_Example_VBNET.htm)

# Requirements

This property only supports model documents saved in SOLIDWORKS 2012 and later.

# See Also

#### 

[ISwDMTable4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4.md)
  
[ISwDMTable4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4_members.md)

# Availability

SOLIDWORKS Document Manager API 2012 SP0

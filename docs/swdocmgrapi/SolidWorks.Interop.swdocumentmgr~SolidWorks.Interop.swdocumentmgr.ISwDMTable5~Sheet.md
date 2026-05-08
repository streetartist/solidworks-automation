# Sheet Property (ISwDMTable5)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable5~Sheet`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable5~Sheet.html) on this topic. |
| Sheet Property (ISwDMTable5) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMTable5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable5.md) : Sheet Property (ISwDMTable5) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets the drawing sheet for this table.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property Sheet As SwDMSheet ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMTable5 Dim value As SwDMSheet   value = instance.Sheet ``` | |

| C# |  |
| --- | --- |
| ``` SwDMSheet Sheet {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property SwDMSheet^ Sheet {    SwDMSheet^ get(); } ``` | |

#### Property Value

[ISwDMSheet](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMTable5::Sheet](swdocumentmgr~SwDMTable5~Sheet.md).

# Example

See the [ISwDMTable5](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable5.md) examples.

# Remarks

This property works only with documents saved in SOLIDWORKS 2017 or later.

# See Also

#### 

[ISwDMTable5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable5.md)
  
[ISwDMTable5 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable5_members.md)

# Availability

SOLIDWORKS Document Manager API 2017 FCS

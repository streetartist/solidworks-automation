# ShowChildComponentsInBOM2 Property (ISwDMConfiguration15)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration15~ShowChildComponentsInBOM2`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration15~ShowChildComponentsInBOM2.html) on this topic. |
| ShowChildComponentsInBOM2 Property (ISwDMConfiguration15) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration15 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration15.md) : ShowChildComponentsInBOM2 Property (ISwDMConfiguration15) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets whether to show child components in the bill of materials (BOM) for this configuration.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Property ShowChildComponentsInBOM2 As System.Integer ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration15 Dim value As System.Integer   instance.ShowChildComponentsInBOM2 = value   value = instance.ShowChildComponentsInBOM2 ``` | |

| C# |  |
| --- | --- |
| ``` System.int ShowChildComponentsInBOM2 {get; set;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.int ShowChildComponentsInBOM2 {    System.int get();    void set ( &   System.int value); } ``` | |

#### Property Value

Show child components in BOM as defined in [swDmShowChildComponentsInBOMResult](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDmShowChildComponentsInBOMResult.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration15::ShowChildComponentsInBOM2](swdocumentmgr~SwDMConfiguration15~ShowChildComponentsInBOM2.md).

# Remarks

This property only supports documents saved in SOLIDWORKS 2009 and later.

# See Also

#### 

[ISwDMConfiguration15 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration15.md)
  
[ISwDMConfiguration15 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration15_members.md)

# Availability

SOLIDWORKS Document Manager API 2018 SP0

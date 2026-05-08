# Delete Property (ISwDMConfiguration7)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~Delete`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~Delete.html) on this topic. |
| Delete Property (ISwDMConfiguration7) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMConfiguration7 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7.md) : Delete Property (ISwDMConfiguration7) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets or sets whether to mark this configuration as deleted.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Property Delete As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMConfiguration7 Dim value As System.Boolean   instance.Delete = value   value = instance.Delete ``` | |

| C# |  |
| --- | --- |
| ``` System.bool Delete {get; set;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.bool Delete {    System.bool get();    void set ( &   System.bool value); } ``` | |

#### Property Value

True marks this configuration as deleted, false does not

# Visual Basic for Applications (VBA) Syntax

See [SwDMConfiguration7::Delete](swdocumentmgr~SwDMConfiguration7~Delete.md).

# See Also

#### 

[ISwDMConfiguration7 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7.md)
  
[ISwDMConfiguration7 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7_members.md)

# Availability

SOLIDWORKS Document Manager API 2007 FCS

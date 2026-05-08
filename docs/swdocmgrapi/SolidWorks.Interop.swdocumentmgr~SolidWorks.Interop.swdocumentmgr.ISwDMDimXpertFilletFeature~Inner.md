# Inner Property (ISwDMDimXpertFilletFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFilletFeature~Inner`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFilletFeature~Inner.html) on this topic. |
| Inner Property (ISwDMDimXpertFilletFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertFilletFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFilletFeature.md) : Inner Property (ISwDMDimXpertFilletFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets whether this DimXpert fillet is for a hole or a pin.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property Inner As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertFilletFeature Dim value As System.Boolean   value = instance.Inner ``` | |

| C# |  |
| --- | --- |
| ``` System.bool Inner {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.bool Inner {    System.bool get(); } ``` | |

#### Property Value

True if the fillet is for a hole; false if for a pin

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertFilletFeature::Inner](swdocumentmgr~SwDMDimXpertFilletFeature~Inner.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertFilletFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFilletFeature.md)
  
[ISwDMDimXpertFilletFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFilletFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

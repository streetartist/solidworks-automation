# Inner Property (ISwDMDimXpertConeFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeFeature~Inner`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeFeature~Inner.html) on this topic. |
| Inner Property (ISwDMDimXpertConeFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertConeFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeFeature.md) : Inner Property (ISwDMDimXpertConeFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Gets whether this DimXpert cone is a hole or a pin.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` ReadOnly Property Inner As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertConeFeature Dim value As System.Boolean   value = instance.Inner ``` | |

| C# |  |
| --- | --- |
| ``` System.bool Inner {get;} ``` | |

| C++/CLI |  |
| --- | --- |
| ``` property System.bool Inner {    System.bool get(); } ``` | |

#### Property Value

True if the cone is a hole; false if it's a pin

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertConeFeature::Inner](swdocumentmgr~SwDMDimXpertConeFeature~Inner.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertConeFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeFeature.md)
  
[ISwDMDimXpertConeFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

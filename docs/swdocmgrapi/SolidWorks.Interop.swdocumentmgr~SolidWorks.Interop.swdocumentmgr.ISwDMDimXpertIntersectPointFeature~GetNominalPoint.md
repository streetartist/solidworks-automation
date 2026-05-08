# GetNominalPoint Method (ISwDMDimXpertIntersectPointFeature)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature~GetNominalPoint`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature~GetNominalPoint.html) on this topic. |
| GetNominalPoint Method (ISwDMDimXpertIntersectPointFeature) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMDimXpertIntersectPointFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature.md) : GetNominalPoint Method (ISwDMDimXpertIntersectPointFeature) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*X*
:   x coordinate of the intersect point

*Y*
:   y coordinate of the intersect point

*Z*
:   z coordinate of the intersect point

Gets the coordinates of this DimXpert intersect point.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetNominalPoint( _    ByRef X As System.Double, _    ByRef Y As System.Double, _    ByRef Z As System.Double _ ) As System.Boolean ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertIntersectPointFeature Dim X As System.Double Dim Y As System.Double Dim Z As System.Double Dim value As System.Boolean   value = instance.GetNominalPoint(X, Y, Z) ``` | |

| C# |  |
| --- | --- |
| ``` System.bool GetNominalPoint(     out System.double X,    out System.double Y,    out System.double Z ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` System.bool GetNominalPoint(  &   [Out] System.double X, &   [Out] System.double Y, &   [Out] System.double Z ) ``` | |

#### Parameters

*X*
:   x coordinate of the intersect point

*Y*
:   y coordinate of the intersect point

*Z*
:   z coordinate of the intersect point

#### Return Value

True if method call is successful; false otherwise

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertIntersectPointFeature::GetNominalPoint](swdocumentmgr~SwDMDimXpertIntersectPointFeature~GetNominalPoint.md).

# Example

See the examples on the interface page.

# See Also

#### 

[ISwDMDimXpertIntersectPointFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature.md)
  
[ISwDMDimXpertIntersectPointFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature_members.md)

# Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

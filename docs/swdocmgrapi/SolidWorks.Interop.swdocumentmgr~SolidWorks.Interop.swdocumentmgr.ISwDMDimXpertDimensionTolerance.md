# ISwDMDimXpertDimensionTolerance Interface

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance.html) on this topic. |
| ISwDMDimXpertDimensionTolerance Interface | |
| [See Also](#seealsobookmark)  [Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance_members.md)   [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) : ISwDMDimXpertDimensionTolerance Interface |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Allows you to access general information about DimXpert dimension tolerances.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Public Interface ISwDMDimXpertDimensionTolerance ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertDimensionTolerance ``` | |

| C# |  |
| --- | --- |
| ``` public interface ISwDMDimXpertDimensionTolerance ``` | |

| C++/CLI |  |
| --- | --- |
| ``` public interface class ISwDMDimXpertDimensionTolerance ``` | |

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertDimensionTolerance](swdocumentmgr~SwDMDimXpertDimensionTolerance.md).

# Example

[Get DimXpert Tolerance (VB.NET)](Get_DimXpert_Tolerance_Example_VBNET.htm)
  
[Get DimXpert Tolerance (C#)](Get_DimXpert_Tolerance_Example_CSharp.htm)

# Remarks

This interface is the base class for several more specific interfaces. (See the **See Also** section.) You can access more general information from [ISwDMDimXpertAnnotation](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation.md). Use the [ISwDMDimXpertAnnotation::type](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~type.md) property to find out which specific interface is needed to acquire more information for a given DimXpert tolerance type.

# Accessors

[ISwDMDimXpertPart::GetAnnotations](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart~GetAnnotations.md) and [ISwDMDimXpertPart::IGetAnnotations](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart~IGetAnnotations.md)

# See Also

#### 

[ISwDMDimXpertDimensionTolerance Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance_members.md)
  
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md)
  
[ISwDMDimXpertAngleBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAngleBetweenDimTol.md)
  
[ISwDMDimXpertChamferDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferDimTol.md)
  
[ISwDMDimXpertCompositeDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol.md)
  
[ISwDMDimXpertConeAngleDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeAngleDimTol.md)
  
[ISwDMDimXpertCounterBoreDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCounterBoreDimTol.md)
  
[ISwDMDimXpertCounterSinkAngleDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCounterSinkAngleDimTol.md)
  
[ISwDMDimXpertCounterSinkDiameterDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCounterSinkDiameterDimTol.md)
  
[ISwDMDimXpertDepthDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDepthDimTol.md)
  
[ISwDMDimXpertDiameterDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDiameterDimTol.md)
  
[ISwDMDimXpertDistanceBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol.md)
  
[ISwDMDimXpertLengthDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertLengthDimTol.md)
  
[ISwDMDimXpertRadiusDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertRadiusDimTol.md)
  
[ISwDMDimXpertWidthDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertWidthDimTol.md)
  
[ISwDMDimXpertPatternAngleBetweenDimTol Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPatternAngleBetweenDimTol.md)

# ISwDMDimXpertAnnotation Interface

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation.html) on this topic. |
| ISwDMDimXpertAnnotation Interface | |
| [See Also](#seealsobookmark)  [Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation_members.md)   [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) : ISwDMDimXpertAnnotation Interface |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Allows you to access general information about DimXpert geometric tolerance, dimension tolerance, and datum annotations.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Public Interface ISwDMDimXpertAnnotation ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertAnnotation ``` | |

| C# |  |
| --- | --- |
| ``` public interface ISwDMDimXpertAnnotation ``` | |

| C++/CLI |  |
| --- | --- |
| ``` public interface class ISwDMDimXpertAnnotation ``` | |

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertAnnotation](swdocumentmgr~SwDMDimXpertAnnotation.md).

# Example

[Get DimXpert Sphere and Datum (VB.NET)](Get_DimXpert_Sphere_and_Datum_Example_VBNET.htm)
  
[Get DimXpert Sphere and Datum (C#)](Get_DimXpert_Sphere_and_Datum_Example_CSharp.htm)

# Remarks

This interface is the base class for three types of annotation interface: [ISwDMDimXpertGeometricTolerance](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertGeometricTolerance.md), [ISwDMDimXpertDimensionTolerance](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDimensionTolerance.md), and [ISwDMDimXpertDatum](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDatum.md). Use the [ISwDMDimXpertAnnotation::type](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~type.md) property to find out which specific interface is needed to acquire more information for a given DimXpert annotation type.

# Accessors

[ISwDMDimXpertPart::GetAnnotations](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart~GetAnnotations.md) and [ISwDMDimXpertPart::IGetAnnotations](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart~IGetAnnotations.md)

# See Also

#### 

[ISwDMDimXpertAnnotation Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation_members.md)
  
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md)

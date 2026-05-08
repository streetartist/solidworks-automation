# ISwDMDimXpertFeature Interface

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature.html) on this topic. |
| ISwDMDimXpertFeature Interface | |
| [See Also](#seealsobookmark)  [Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature_members.md)   [Example](#ExampleBookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) : ISwDMDimXpertFeature Interface |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

Allows you to access general information about DimXpert features and sub-features.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Public Interface ISwDMDimXpertFeature ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMDimXpertFeature ``` | |

| C# |  |
| --- | --- |
| ``` public interface ISwDMDimXpertFeature ``` | |

| C++/CLI |  |
| --- | --- |
| ``` public interface class ISwDMDimXpertFeature ``` | |

# Visual Basic for Applications (VBA) Syntax

See [SwDMDimXpertFeature](swdocumentmgr~SwDMDimXpertFeature.md).

# Example

[Get DimXpert Sphere and Datum (VB.NET)](Get_DimXpert_Sphere_and_Datum_Example_VBNET.htm)
  
[Get DimXpert Sphere and Datum (C#)](Get_DimXpert_Sphere_and_Datum_Example_CSharp.htm)

# Remarks

This interface is the base class for several more specific DimXpert feature interfaces (see the **See Also** section). Use the [ISwDMDimXpertFeature::type](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature~type.md) property to find out which specific feature interface is needed to acquire more information for a given DimXpert feature.

# Accessors

[ISwDMDimXpertAngleBetweenDimTol::OriginFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAngleBetweenDimTol~OriginFeature.md)

[ISwDMDimXpertAnnotation::Feature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertAnnotation~Feature.md)

[ISwDMDimXpertBestFitPlaneFeature::GetSubFeatures](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBestFitPlaneFeature~GetSubFeatures.md) and [ISwDMDimXpertBestFitPlaneFeature::IGetSubFeatures](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBestFitPlaneFeature~IGetSubFeatures.md)

[ISwDMDimXpertCompositeDistanceBetweenDimTol::GetFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~GetFeature.md), [ISwDMDimXpertCompositeDistanceBetweenDimTol::GetIntraFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~GetIntraFeature.md), [ISwDMDimXpertCompositeDistanceBetweenDimTol::GetOriginFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompositeDistanceBetweenDimTol~GetOriginFeature.md)

[ISwDMDimXpertCompoundClosedSlot3DFeature::GetBottomFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundClosedSlot3dFeature~GetBottomFeature.md) and [ISwDMDimXpertCompoundClosedSlot3DFeature::GetEndFeatures](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundClosedSlot3dFeature~GetEndFeatures.md)

[ISwDMDimXpertCompoundHoleFeature::GetBottomFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature~GetBottomFeature.md), [ISwDMDimXpertCompoundHoleFeature::GetReferenceFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature~GetReferenceFeature.md), [ISwDMDimXpertCompoundHoleFeature::GetSubFeatures](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature~GetSubFeatures.md), [ISwDMDimXpertCompoundHoleFeature::IGetSubFeatures](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature~IGetSubFeatures.md)

[ISwDMDimXpertCompoundNotchFeature::GetBottomFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature~GetBottomFeature.md), [ISwDMDimXpertCompoundNotchFeature::GetEndFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature~GetEndFeature.md), [ISwDMDimXpertCompoundNotchFeature::GetOpenSideReferenceFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature~GetOpenSideReferenceFeature.md), [ISwDMDimXpertCompoundNotchFeature::GetTopReferenceFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature~GetTopReferenceFeature.md)

[ISwDMDimXpertCounterBoreDimTol::ReferenceFeature property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCounterBoreDimTol~ReferenceFeature.md)

[ISwDMDimXpertCounterSinkAngleDimTol::ReferenceFeature property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCounterSinkAngleDimTol~ReferenceFeature.md)

[ISwDMDimXpertCounterSinkDiameterDimTol::ReferenceFeature property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCounterSinkDiameterDimTol~ReferenceFeature.md)

[ISwDMDimXpertDepthDimTol::ReferenceFeature property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDepthDimTol~ReferenceFeature.md)

[ISwDMDimXpertDistanceBetweenDimTol::GetFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol~GetFeature.md) and [ISwDMDimXpertDistanceBetweenDimTol::GetOriginFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertDistanceBetweenDimTol~GetOriginFeature.md)

[ISwDMDimXpertExtrudeFeature::GetBottomBlends](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~GetBottomBlends.md), [ISwDMDimXpertExtrudeFeature::GetTopBlends](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~GetTopBlends.md), [ISwDMDimXpertExtrudeFeature::GetBottomFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~GetBottomFeature.md), [ISwDMDimXpertExtrudeFeature::GetReferenceFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~GetReferenceFeature.md), [ISwDMDimXpertExtrudeFeature::GetSubFeatures](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~GetSubFeatures.md), [ISwDMDimXpertExtrudeFeature::IGetSubFeatures](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature~IGetSubFeatures.md)

[ISwDMDimXpertIntersectCircleFeature::GetIntersectFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectCircleFeature~GetIntersectFeature.md) and [ISwDMDimXpertIntersectCircleFeature::GetPlaneFeature](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectCircleFeature~GetPlaneFeature.md)

[ISwDMDimXpertIntersectLineFeature::GetPlaneFeatures](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectLineFeature~GetPlaneFeatures.md)

[ISwDMDimXpertIntersectPlaneFeature::GetFeatures](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPlaneFeature~GetFeatures.md)

[ISwDMDimXpertIntersectPointFeature::GetFeatures](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature~GetFeatures.md)

[ISwDMDimXpertPart::GetFeatures](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart~GetFeatures.md) and [ISwDMDimXpertPart::IGetFeatures](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPart~IGetFeatures.md)

[ISwDMDimXpertPatternFeature::GetSubFeatures](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPatternFeature~GetSubFeatures.md) and [ISwDMDimXpertPatternFeature::IGetSubFeatures](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPatternFeature~IGetSubFeatures.md)

[ISwDMDimXpertTangencyTolerance::GetOriginFeature property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertTangencyGeoTol~GetOriginFeature.md)

# See Also

#### 

[ISwDMDimXpertFeature Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFeature_members.md)
  
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md)
  
[ISwDMDimXpertBestFitPlaneFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertBestFitPlaneFeature.md)
  
[ISwDMDimXpertChamferFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertChamferFeature.md)
  
[ISwDMDimXpertCompoundClosedSlot3dFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundClosedSlot3dFeature.md)
  
[ISwDMDimXpertCompoundHoleFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundHoleFeature.md)
  
[ISwDMDimXpertCompoundNotchFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundNotchFeature.md)
  
[ISwDMDimXpertCompoundWidthFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCompoundWidthFeature.md)
  
[ISwDMDimXpertConeFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertConeFeature.md)
  
[ISwDMDimXpertCylinderFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertCylinderFeature.md)
  
[ISwDMDimXpertExtrudeFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertExtrudeFeature.md)
  
[ISwDMDimXpertFilletFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertFilletFeature.md)
  
[ISwDMDimXpertIntersectCircleFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectCircleFeature.md)
  
[ISwDMDimXpertIntersectLineFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectLineFeature.md)
  
[ISwDMDimXpertIntersectPlaneFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPlaneFeature.md)
  
[ISwDMDimXpertIntersectPointFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertIntersectPointFeature.md)
  
[ISwDMDimXpertPatternFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPatternFeature.md)
  
[ISwDMDimXpertPlaneFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertPlaneFeature.md)
  
[ISwDMDimXpertSphereFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSphereFeature.md)
  
[ISwDMDimXpertSurfaceFeature Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDimXpertSurfaceFeature.md)

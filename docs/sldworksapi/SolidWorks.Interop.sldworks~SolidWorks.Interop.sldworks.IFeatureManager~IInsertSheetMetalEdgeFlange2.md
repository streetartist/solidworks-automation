# IInsertSheetMetalEdgeFlange2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertSheetMetalEdgeFlange2`

Obsolete. Superseded by IFeatureManager::CreateDefinition and IFeatureManager::CreateFeature.
Obsolete. Superseded by [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md) and [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertSheetMetalEdgeFlange2( _
   ByVal EdgeCount As System.Integer, _
   ByRef FlangeEdges As Edge, _
   ByVal SketchFeatCount As System.Integer, _
   ByRef SketchFeat As Feature, _
   ByVal BooleanOptions As System.Integer, _
   ByVal FlangeAngle As System.Double, _
   ByVal FlangeRadius As System.Double, _
   ByVal BendPosition As System.Integer, _
   ByVal FlangeOffsetDist As System.Double, _
   ByVal ReliefType As System.Integer, _
   ByVal FlangeReliefRatio As System.Double, _
   ByVal FlangeReliefWidth As System.Double, _
   ByVal FlangeReliefDepth As System.Double, _
   ByVal FlangeSharpType As System.Integer, _
   ByVal CustomBendAllowance As CustomBendAllowance _
) As Feature
```

```

Dim instance As IFeatureManager
Dim EdgeCount As System.Integer
Dim FlangeEdges As Edge
Dim SketchFeatCount As System.Integer
Dim SketchFeat As Feature
Dim BooleanOptions As System.Integer
Dim FlangeAngle As System.Double
Dim FlangeRadius As System.Double
Dim BendPosition As System.Integer
Dim FlangeOffsetDist As System.Double
Dim ReliefType As System.Integer
Dim FlangeReliefRatio As System.Double
Dim FlangeReliefWidth As System.Double
Dim FlangeReliefDepth As System.Double
Dim FlangeSharpType As System.Integer
Dim CustomBendAllowance As CustomBendAllowance
Dim value As Feature
 
value = instance.IInsertSheetMetalEdgeFlange2(EdgeCount, FlangeEdges, SketchFeatCount, SketchFeat, BooleanOptions, FlangeAngle, FlangeRadius, BendPosition, FlangeOffsetDist, ReliefType, FlangeReliefRatio, FlangeReliefWidth, FlangeReliefDepth, FlangeSharpType, CustomBendAllowance)
```

```

Feature IInsertSheetMetalEdgeFlange2( 
   System.int EdgeCount,
   ref Edge FlangeEdges,
   System.int SketchFeatCount,
   ref Feature SketchFeat,
   System.int BooleanOptions,
   System.double FlangeAngle,
   System.double FlangeRadius,
   System.int BendPosition,
   System.double FlangeOffsetDist,
   System.int ReliefType,
   System.double FlangeReliefRatio,
   System.double FlangeReliefWidth,
   System.double FlangeReliefDepth,
   System.int FlangeSharpType,
   CustomBendAllowance CustomBendAllowance
)
```

```

Feature^ IInsertSheetMetalEdgeFlange2( 
   System.int EdgeCount,
   Edge^% FlangeEdges,
   System.int SketchFeatCount,
   Feature^% SketchFeat,
   System.int BooleanOptions,
   System.double FlangeAngle,
   System.double FlangeRadius,
   System.int BendPosition,
   System.double FlangeOffsetDist,
   System.int ReliefType,
   System.double FlangeReliefRatio,
   System.double FlangeReliefWidth,
   System.double FlangeReliefDepth,
   System.int FlangeSharpType,
   CustomBendAllowance^ CustomBendAllowance
) 
```

#### Parameters

*EdgeCount*
:   Number of edges for the flange

*FlangeEdges*
:   Array of edge to which to apply a flange

*SketchFeatCount*
:   Number of sketches for the flange

*SketchFeat*
:   Array of sketch [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) to use for the flange

*BooleanOptions*
:   Flange options as defined by [swInsertEdgeFlangeOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInsertEdgeFlangeOptions_e.html)

*FlangeAngle*
:   Flange angle

*FlangeRadius*
:   Bend radius

*BendPosition*
:   Flange bend position as defined by [swFlangePositionTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangePositionTypes_e.html)

*FlangeOffsetDist*
:   Length of flange

*ReliefType*
:   Relief type as defined by [swSheetMetalReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html)

*FlangeReliefRatio*
:   Relief ratio

*FlangeReliefWidth*
:   Relief width

*FlangeReliefDepth*
:   Relief depth

*FlangeSharpType*
:   Flange virtual sharp type as defined by [swFlangeDimTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangeDimTypes_e.html)

*CustomBendAllowance*
:   |  |  |
    | --- | --- |
    | **If...** | **Then...** |
    | non-NULL | Pointer to [ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md) object for which required values have been set |
    | NULL | Parent bend's bend allowance is used |

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

Before calling this method, call [IModelDoc2::IInsertSketchForEdgeFlange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertSketchForEdgeFlange.md) and create a profile for the flange. After creating the profile, call this method to create the flange.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::InsertSheetMetalEdgeFlange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSheetMetalEdgeFlange.md)  
[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md)

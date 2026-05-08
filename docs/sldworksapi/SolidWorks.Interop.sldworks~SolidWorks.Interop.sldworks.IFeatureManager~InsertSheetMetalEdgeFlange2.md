# InsertSheetMetalEdgeFlange2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalEdgeFlange2`

Obsolete. Superseded by IFeatureManager::CreateDefinition and IFeatureManager::CreateFeature.
Obsolete. Superseded by [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md) and [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSheetMetalEdgeFlange2( _
   ByVal FlangeEdges As System.Object, _
   ByVal SketchFeats As System.Object, _
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
Dim FlangeEdges As System.Object
Dim SketchFeats As System.Object
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
 
value = instance.InsertSheetMetalEdgeFlange2(FlangeEdges, SketchFeats, BooleanOptions, FlangeAngle, FlangeRadius, BendPosition, FlangeOffsetDist, ReliefType, FlangeReliefRatio, FlangeReliefWidth, FlangeReliefDepth, FlangeSharpType, CustomBendAllowance)
```

```

Feature InsertSheetMetalEdgeFlange2( 
   System.object FlangeEdges,
   System.object SketchFeats,
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

Feature^ InsertSheetMetalEdgeFlange2( 
   System.Object^ FlangeEdges,
   System.Object^ SketchFeats,
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

*FlangeEdges*
:   Array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) to which to apply a flange

*SketchFeats*
:   Array of [sketches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md) to use for the flange

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

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md) object

Remarks

Before calling this method, call [IModelDoc2::InsertSketchForEdgeFlange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchForEdgeFlange.md) and create a profile for the flange. After creating the profile, call this method to create the flange.

Example

[Insert Sheet Metal Edge Flange (VBA)](Insert_Sheet_Metal_Edge_Flange_Example_VB.htm)  
[Create Corner Relief Feature (C#)](Create_Corner_Relief_Feature_Example_CSharp.htm)  
[Create Corner Relief Feature (VBA)](Create_Corner_Relief_Feature_Example_VB.htm)  
[Create Corner Relief Feature (VB.NET)](Create_Corner_Relief_Feature_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.md)  
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md)

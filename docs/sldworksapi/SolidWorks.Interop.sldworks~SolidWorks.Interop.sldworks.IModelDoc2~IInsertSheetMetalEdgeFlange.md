# IInsertSheetMetalEdgeFlange Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertSheetMetalEdgeFlange`

Obsolete. Superseded by IFeatureManager::InsertSheetMetalEdgeFlange2.
Obsolete. Superseded by [IFeatureManager::InsertSheetMetalEdgeFlange2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalEdgeFlange2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertSheetMetalEdgeFlange( _
   ByVal FlangeEdge As Edge, _
   ByVal SketchFeat As Feature, _
   ByVal BooleanOptions As System.Integer, _
   ByVal DAngle As System.Double, _
   ByVal DRadius As System.Double, _
   ByVal BendPosition As System.Integer, _
   ByVal DOffsetDist As System.Double, _
   ByVal ReliefType As System.Integer, _
   ByVal DReliefRatio As System.Double, _
   ByVal DReliefWidth As System.Double, _
   ByVal DReliefDepth As System.Double _
) As Feature
```

```

Dim instance As IModelDoc2
Dim FlangeEdge As Edge
Dim SketchFeat As Feature
Dim BooleanOptions As System.Integer
Dim DAngle As System.Double
Dim DRadius As System.Double
Dim BendPosition As System.Integer
Dim DOffsetDist As System.Double
Dim ReliefType As System.Integer
Dim DReliefRatio As System.Double
Dim DReliefWidth As System.Double
Dim DReliefDepth As System.Double
Dim value As Feature
 
value = instance.IInsertSheetMetalEdgeFlange(FlangeEdge, SketchFeat, BooleanOptions, DAngle, DRadius, BendPosition, DOffsetDist, ReliefType, DReliefRatio, DReliefWidth, DReliefDepth)
```

```

Feature IInsertSheetMetalEdgeFlange( 
   Edge FlangeEdge,
   Feature SketchFeat,
   System.int BooleanOptions,
   System.double DAngle,
   System.double DRadius,
   System.int BendPosition,
   System.double DOffsetDist,
   System.int ReliefType,
   System.double DReliefRatio,
   System.double DReliefWidth,
   System.double DReliefDepth
)
```

```

Feature^ IInsertSheetMetalEdgeFlange( 
   Edge^ FlangeEdge,
   Feature^ SketchFeat,
   System.int BooleanOptions,
   System.double DAngle,
   System.double DRadius,
   System.int BendPosition,
   System.double DOffsetDist,
   System.int ReliefType,
   System.double DReliefRatio,
   System.double DReliefWidth,
   System.double DReliefDepth
) 
```

#### Parameters

*FlangeEdge*

*SketchFeat*

*BooleanOptions*

*DAngle*

*DRadius*

*BendPosition*

*DOffsetDist*

*ReliefType*

*DReliefRatio*

*DReliefWidth*

*DReliefDepth*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)

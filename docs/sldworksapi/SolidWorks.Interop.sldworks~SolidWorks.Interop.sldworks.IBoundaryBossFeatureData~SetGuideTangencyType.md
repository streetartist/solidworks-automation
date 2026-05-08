# SetGuideTangencyType Method (IBoundaryBossFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetGuideTangencyType`

Sets the type of tangency for the specified curve in the specified direction in this boundary feature.
Sets the type of tangency for the specified curve in the specified direction in this boundary feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetGuideTangencyType( _
   ByVal Direction As System.Integer, _
   ByVal GuideIndex As System.Integer, _
   ByVal TangType As System.Integer _
) 
```

```

Dim instance As IBoundaryBossFeatureData
Dim Direction As System.Integer
Dim GuideIndex As System.Integer
Dim TangType As System.Integer
 
instance.SetGuideTangencyType(Direction, GuideIndex, TangType)
```

```

void SetGuideTangencyType( 
   System.int Direction,
   System.int GuideIndex,
   System.int TangType
)
```

```

void SetGuideTangencyType( 
   System.int Direction,
   System.int GuideIndex,
   System.int TangType
) 
```

#### Parameters

*Direction*
:   Direction as defined in [swBoundaryBossDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossDirection_e.html)

*GuideIndex*
:   Index of the curve (see **Remarks**)

*TangType*
:   Type of tangency as defined in [swBoundaryBossTangencyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossTangencyType_e.html)

Remarks

This method is only available when a minimum of three curves in the specified direction exist.

Call [IBoundaryBossFeatureData::GetCurvesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetCurvesCount.md) to get a valid range of values for GuideIndex.

| If specified curve is... | Then the valid types of tangency as defined in swBoundaryBossTangencyType\_e are... |
| --- | --- |
| [Sketch curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md) | - swBoundaryBossTangency\_None - swBoundaryBossTangency\_DirectionVector - swBoundaryBossTangency\_NormalToProfile |
| [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) | - swBoundaryBossTangency\_None - swBoundaryBossTangency\_DirectionVector - swBoundaryBossTangency\_NormalToProfile - swBoundaryBossTangency\_TangencyToFace - swBoundaryBossTangency\_CurvatureToFace |
| [Edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) | - swBoundaryBossTangency\_Default - swBoundaryBossTangency\_None - swBoundaryBossTangency\_DirectionVector - swBoundaryBossTangency\_TangencyToFace - swBoundaryBossTangency\_CurvatureToFace |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.md)  
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.md)  
[IBoundaryBossFeatureData::GetGuideTangencyType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetGuideTangencyType.md)  
[IBoundaryBossFeatureData::GetTangentApplyToAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentApplyToAll.md)  
[IBoundaryBossFeatureData::GetTangentDirectionReversed Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentDirectionReversed.md)  
[IBoundaryBossFeatureData::GetTangentInfluence Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentInfluence.md)  
[IBoundaryBossFeatureData::GetTangentLength Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetTangentLength.md)  
[IBoundaryBossFeatureData::SetTangentApplyToAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentApplyToAll.md)  
[IBoundaryBossFeatureData::SetTangentDirectionReversed Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentDirectionReversed.md)  
[IBoundaryBossFeatureData::SetTangentInfluence Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentInfluence.md)  
[IBoundaryBossFeatureData::SetTangentLength Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetTangentLength.md)  
[IBoundaryBossFeatureData::MergeTangentFaces Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~MergeTangentFaces.md)

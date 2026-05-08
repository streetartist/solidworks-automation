# SetDirectionVector Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetDirectionVector`

Sets the entity to use as the direction vector for the specified curve in the specified direction in this boundary feature.
Sets the entity to use as the direction vector for the specified curve in the specified direction in this boundary feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetDirectionVector( _
   ByVal Direction As System.Integer, _
   ByVal GuideIndex As System.Integer, _
   ByVal DirectionVector As System.Object _
) 
```

```

Dim instance As IBoundaryBossFeatureData
Dim Direction As System.Integer
Dim GuideIndex As System.Integer
Dim DirectionVector As System.Object
 
instance.SetDirectionVector(Direction, GuideIndex, DirectionVector)
```

```

void SetDirectionVector( 
   System.int Direction,
   System.int GuideIndex,
   System.object DirectionVector
)
```

```

void SetDirectionVector( 
   System.int Direction,
   System.int GuideIndex,
   System.Object^ DirectionVector
) 
```

#### Parameters

*Direction*
:   Direction as defined in [swBoundaryBossDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossDirection_e.html)

*GuideIndex*
:   Index of the curve (see **Remarks**)

*DirectionVector*
:   Entity to use as the direction vector:

    - linear [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)
    - [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md)
    - [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)
    - [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)

Remarks

This method is only available if the type of tangency of the direction vector is [swBoundaryBossTangencyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossTangencyType_e.html).swBoundaryBossTangency\_DirectionVector. Use [IBoundaryBossFeatureData::GetGuideTangencyType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetGuideTangencyType.md) to determine the type of tangency.

Call [IBoundaryBossFeatureData::GetCurvesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetCurvesCount.md) to get a valid range of values for GuideIndex.

**NOTE:** Using two vertices for the direction vector is not currently supported by the SOLIDWORKS API.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.md)  
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.md)  
[IBoundaryBossFeatureData::GetDirectionVector Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetDirectionVector.md)

# SetAlignmentType Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetAlignmentType`

Sets the type of alignment for the specified curve in the specified direction for this boundary feature.
Sets the type of alignment for the specified curve in the specified direction for this boundary feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetAlignmentType( _
   ByVal Direction As System.Integer, _
   ByVal GuideIndex As System.Integer, _
   ByVal AlignmentType As System.Integer _
) 
```

```

Dim instance As IBoundaryBossFeatureData
Dim Direction As System.Integer
Dim GuideIndex As System.Integer
Dim AlignmentType As System.Integer
 
instance.SetAlignmentType(Direction, GuideIndex, AlignmentType)
```

```

void SetAlignmentType( 
   System.int Direction,
   System.int GuideIndex,
   System.int AlignmentType
)
```

```

void SetAlignmentType( 
   System.int Direction,
   System.int GuideIndex,
   System.int AlignmentType
) 
```

#### Parameters

*Direction*
:   Direction as defined in [swBoundaryBossDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossDirection_e.html)

*GuideIndex*
:   Index of the curve (see **Remarks**)

*AlignmentType*
:   Type of alignment as defined in [swBoundaryBossAlignment\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossAlignment_e.html)

Remarks

This method is only available for a single-direction boundary feature.

You must use the appropriate combination of tangents and alignments.

| Type of [tangency](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetGuideTangencyType.md) as defined in [swBoundaryBossTangencyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossTangencyType_e.html) | Type of alignment as defined in swBoundaryBossAlignment\_e |
| --- | --- |
| swBoundaryBossTangency\_DirectionVector  - or -  swBoundaryBossTangency\_NormalToProfile | - swAlignWithNextSection - swAlignWithSectionNormal |
| swBoundaryBossTangency\_TangencyToFace  -or -  swBoundaryBossTangency\_CurvatureToFace | - swAlignWithNextSection - swAlignWithSectionNormal - swAlignWithIsoParameter - swAlignWithOtherGeometry |

Call [IBoundaryBossFeatureData::GetCurvesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetCurvesCount.md) to get a valid range of values for GuideIndex.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.md)  
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.md)  
[IBoundaryBossFeatureData::GetAlignmentType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetAlignmentType.md)

# SetDraftAngleReverseDirection Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetDraftAngleReverseDirection`

Sets whether the draft angle is flipped for the specified curve in the specified direction in this boundary feature.
Sets whether the draft angle is flipped for the specified curve in the specified direction in this boundary feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetDraftAngleReverseDirection( _
   ByVal Direction As System.Integer, _
   ByVal GuideIndex As System.Integer, _
   ByVal IsFlipped As System.Boolean _
) 
```

```

Dim instance As IBoundaryBossFeatureData
Dim Direction As System.Integer
Dim GuideIndex As System.Integer
Dim IsFlipped As System.Boolean
 
instance.SetDraftAngleReverseDirection(Direction, GuideIndex, IsFlipped)
```

```

void SetDraftAngleReverseDirection( 
   System.int Direction,
   System.int GuideIndex,
   System.bool IsFlipped
)
```

```

void SetDraftAngleReverseDirection( 
   System.int Direction,
   System.int GuideIndex,
   System.bool IsFlipped
) 
```

#### Parameters

*Direction*
:   Direction as defined in [swBoundaryBossDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossDirection_e.html)

*GuideIndex*
:   Index of the curve (see **Remarks**)

*IsFlipped*
:   True if the draft angle is flipped, false if not

Remarks

Call [IBoundaryBossFeatureData::GetCurvesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetCurvesCount.md) to get a valid range of values for GuideIndex.

Example

[Insert Boundary Feature (C#)](Insert_Boundary_Feature_Example_CSharp.htm)  
[Insert Boundary Feature (VB.NET)](Insert_Boundary_Feature_Example_VBNET.htm)  
[Insert Boundary Feature (VBA)](Insert_Boundary_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.md)  
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.md)  
[IBoundaryBossFeatureData::GetDraftAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetDraftAngle.md)  
[IBoundaryBossFeatureData::GetDraftAngleReverseDirection Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetDraftAngleReverseDirection.md)  
[IBoundaryBossFeatureData::SetDraftAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetDraftAngle.md)

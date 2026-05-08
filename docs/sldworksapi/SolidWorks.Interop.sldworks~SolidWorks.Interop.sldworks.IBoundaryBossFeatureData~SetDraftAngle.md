# SetDraftAngle Method (IBoundaryBossFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetDraftAngle`

Sets the draft angle for the specified curve in the specified direction in this boundary feature.
Sets the draft angle for the specified curve in the specified direction in this boundary feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetDraftAngle( _
   ByVal Direction As System.Integer, _
   ByVal GuideIndex As System.Integer, _
   ByVal DraftAngle As System.Double _
) 
```

```

Dim instance As IBoundaryBossFeatureData
Dim Direction As System.Integer
Dim GuideIndex As System.Integer
Dim DraftAngle As System.Double
 
instance.SetDraftAngle(Direction, GuideIndex, DraftAngle)
```

```

void SetDraftAngle( 
   System.int Direction,
   System.int GuideIndex,
   System.double DraftAngle
)
```

```

void SetDraftAngle( 
   System.int Direction,
   System.int GuideIndex,
   System.double DraftAngle
) 
```

#### Parameters

*Direction*
:   Direction as defined in [swBoundaryBossDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossDirection_e.html)

*GuideIndex*
:   Index of the curve (see **Remarks**)

*DraftAngle*
:   Draft angle

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
[IBoundaryBossFeatureData::SetDraftAngleReverseDirection Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetDraftAngleReverseDirection.md)

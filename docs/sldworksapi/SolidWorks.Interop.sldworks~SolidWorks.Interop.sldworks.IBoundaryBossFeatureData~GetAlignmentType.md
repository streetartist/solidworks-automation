# GetAlignmentType Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetAlignmentType`

Gets the type of alignment for the specified curve in the specified direction for this boundary feature.
Gets the type of alignment for the specified curve in the specified direction for this boundary feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAlignmentType( _
   ByVal Direction As System.Integer, _
   ByVal GuideIndex As System.Integer _
) As System.Integer
```

```

Dim instance As IBoundaryBossFeatureData
Dim Direction As System.Integer
Dim GuideIndex As System.Integer
Dim value As System.Integer
 
value = instance.GetAlignmentType(Direction, GuideIndex)
```

```

System.int GetAlignmentType( 
   System.int Direction,
   System.int GuideIndex
)
```

```

System.int GetAlignmentType( 
   System.int Direction,
   System.int GuideIndex
) 
```

#### Parameters

*Direction*
:   Direction as defined in [swBoundaryBossDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossDirection_e.html)

*GuideIndex*
:   Index of the curve (see **Remarks**)

#### Return Value

Type of alignment as defined in [swBoundaryBossAlignment\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBoundaryBossAlignment_e.html)

Remarks

This method is only available for a single-direction boundary feature.

Call [IBoundaryBossFeatureData::GetCurvesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~GetCurvesCount.md) to get a valid range of values for GuideIndex.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.md)  
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.md)  
[IBoundaryBossFeatureData::SetAlignmentType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~SetAlignmentType.md)

# MergePoints Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~MergePoints`

Merges sketch points within a specified distance.
Merges sketch points within a specified distance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MergePoints( _
   ByVal Distance As System.Double _
) As System.Boolean
```

```

Dim instance As ISketch
Dim Distance As System.Double
Dim value As System.Boolean
 
value = instance.MergePoints(Distance)
```

```

System.bool MergePoints( 
   System.double Distance
)
```

```

System.bool MergePoints( 
   System.double Distance
) 
```

#### Parameters

*Distance*
:   Distance at which points are considered coincident

#### Return Value

True if successful, false if not

Remarks

This method requires that only one open contour exists in the sketch. To specify a distance below which points are automatically merged while creating the segments, use [ISketchRelationManager::AddRelation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~AddRelation.md) or [ISketchRelationManager::IAddRelation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IAddRelation.md) and swConstraintType\_COINCIDENT.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::IGetSketchPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchPoints2.md)  
[ISketch::GetSketchPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPoints2.md)  
[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)

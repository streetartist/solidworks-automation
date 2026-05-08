# ISetConstraintCurves Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ISetConstraintCurves`

Sets the entities for the constraint curves.
Sets the entities for the constraint curves.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetConstraintCurves( _
   ByVal Count As System.Integer, _
   ByRef DispArr As System.Object _
) 
```

```

Dim instance As IFillSurfaceFeatureData
Dim Count As System.Integer
Dim DispArr As System.Object
 
instance.ISetConstraintCurves(Count, DispArr)
```

```

void ISetConstraintCurves( 
   System.int Count,
   ref System.object DispArr
)
```

```

void ISetConstraintCurves( 
   System.int Count,
   System.Object^% DispArr
) 
```

#### Parameters

*Count*
:   Number of entities to use to constrain the surface

*DispArr*
:   - in-process, unmanaged C++: Pointer to an rray of entities to use to constrain the surface; valid entities are:
      - [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)
      - [sketches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)
    - VBA, VB.NET, C#, and C++/CLI: Not supported
    - See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.md)  
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.md)  
[IFillSurfaceFeatureData::GetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetConstraintCurves.md)  
[IFillSurfaceFeatureData::GetConstraintCurvesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetConstraintCurvesCount.md)  
[IFillSurfaceFeatureData::SetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetConstraintCurves.md)

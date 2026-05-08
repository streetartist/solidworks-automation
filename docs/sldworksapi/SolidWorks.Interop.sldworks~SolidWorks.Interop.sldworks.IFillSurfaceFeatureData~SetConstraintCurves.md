# SetConstraintCurves Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetConstraintCurves`

Sets the entities for the constraint curves.
Sets the entities for the constraint curves.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetConstraintCurves( _
   ByVal ConstraintVar As System.Object _
) 
```

```

Dim instance As IFillSurfaceFeatureData
Dim ConstraintVar As System.Object
 
instance.SetConstraintCurves(ConstraintVar)
```

```

void SetConstraintCurves( 
   System.object ConstraintVar
)
```

```

void SetConstraintCurves( 
   System.Object^ ConstraintVar
) 
```

#### Parameters

*ConstraintVar*
:   Array of entities to use to constrain the surface; valid entities are:

    - [Edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)
    - [Sketches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)

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
[IFillSurfaceFeatureData::IGetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~IGetConstraintCurves.md)  
[IFillSurfaceFeatureData::ISetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ISetConstraintCurves.md)

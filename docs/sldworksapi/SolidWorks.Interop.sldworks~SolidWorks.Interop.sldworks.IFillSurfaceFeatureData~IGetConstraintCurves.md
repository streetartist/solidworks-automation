# IGetConstraintCurves Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~IGetConstraintCurves`

Gets the constraint curves for this fill-surface feature.
Gets the constraint curves for this fill-surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetConstraintCurves( _
   ByVal Count As System.Integer, _
   ByRef TypeArr As System.Integer _
) As System.Object
```

```

Dim instance As IFillSurfaceFeatureData
Dim Count As System.Integer
Dim TypeArr As System.Integer
Dim value As System.Object
 
value = instance.IGetConstraintCurves(Count, TypeArr)
```

```

System.object IGetConstraintCurves( 
   System.int Count,
   out System.int TypeArr
)
```

```

System.Object^ IGetConstraintCurves( 
   System.int Count,
   [Out] System.int TypeArr
) 
```

#### Parameters

*Count*
:   Number of entities used to constrain the surface

*TypeArr*
:   - in-process, unmanaged C++: Pointer to an array of types of entities used to constrain the surface as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html); valid entities are:

      - edges (swSelEDGES)
      - sketches (swSelSKETCHES)
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

- in-process, unmanaged C++: Pointer to an array of entities used as constraint curves

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IFillSurfaceFeatureData::GetConstraintCurvesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetConstraintCurvesCount.md) before calling this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.md)  
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.md)  
[IFillSurfaceFeatureData::GetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetConstraintCurves.md)  
[IFillSurfaceFeatureData::ISetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ISetConstraintCurves.md)  
[IFillSurfaceFeatureData::SetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetConstraintCurves.md)

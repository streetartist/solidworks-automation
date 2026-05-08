# ISetCurves Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~ISetCurves`

Sets the curves for this imported curve feature.
Sets the curves for this imported curve feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetCurves( _
   ByVal Count As System.Integer, _
   ByRef DispArr As System.Object _
) 
```

```

Dim instance As IImportedCurveFeatureData
Dim Count As System.Integer
Dim DispArr As System.Object
 
instance.ISetCurves(Count, DispArr)
```

```

void ISetCurves( 
   System.int Count,
   ref System.object DispArr
)
```

```

void ISetCurves( 
   System.int Count,
   System.Object^% DispArr
) 
```

#### Parameters

*Count*
:   Number of curves

*DispArr*
:   - in-process, unmanaged C++: Pointer to an array of curves of size Count

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportedCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData.md)  
[IImportedCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData_members.md)  
[IImportedCurveFeatureData::GetCurveCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~GetCurveCount.md)  
[IImportedCurveFeatureData::IGetCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~IGetCurves.md)  
[IImportedCurveFeatureData::Curves Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~Curves.md)

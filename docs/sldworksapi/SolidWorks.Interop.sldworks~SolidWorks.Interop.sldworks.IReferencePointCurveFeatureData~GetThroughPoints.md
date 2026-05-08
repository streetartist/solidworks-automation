# GetThroughPoints Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~GetThroughPoints`

Gets the points through which this curve passes.
Gets the points through which this curve passes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetThroughPoints( _
   ByRef Type As System.Object _
) As System.Object
```

```

Dim instance As IReferencePointCurveFeatureData
Dim Type As System.Object
Dim value As System.Object
 
value = instance.GetThroughPoints(Type)
```

```

System.object GetThroughPoints( 
   out System.object Type
)
```

```

System.Object^ GetThroughPoints( 
   [Out] System.Object^ Type
) 
```

#### Parameters

*Type*
:   Type of entities (sketch points or vertices) as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

#### Return Value

Array of points

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IReferencePointCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData.md)  
[IReferencePointCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData_members.md)  
[IReferencePointCurveFeatureData::GetThroughPointCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~GetThroughPointCount.md)  
[IReferencePointCurveFeatureData::IGetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~IGetThroughPoints.md)  
[IReferencePointCurveFeatureData::ISetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~ISetThroughPoints.md)  
[IReferencePointCurveFeatureData::SetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~SetThroughPoints.md)

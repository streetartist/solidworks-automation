# SetThroughPoints Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~SetThroughPoints`

Sets the points through which this curve passes.
Sets the points through which this curve passes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetThroughPoints( _
   ByVal Pts As System.Object _
) 
```

```

Dim instance As IReferencePointCurveFeatureData
Dim Pts As System.Object
 
instance.SetThroughPoints(Pts)
```

```

void SetThroughPoints( 
   System.object Pts
)
```

```

void SetThroughPoints( 
   System.Object^ Pts
) 
```

#### Parameters

*Pts*
:   Array of points

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IReferencePointCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData.md)  
[IReferencePointCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData_members.md)  
[IReferencePointCurveFeatureData::ISetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~ISetThroughPoints.md)  
[IReferencePointCurveFeatureData::GetThroughPointCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~GetThroughPointCount.md)  
[IReferencePointCurveFeatureData::GetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~GetThroughPoints.md)  
[IReferencePointCurveFeatureData::IGetThroughPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~IGetThroughPoints.md)

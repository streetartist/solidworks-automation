# GetEntitiesToJoinCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~GetEntitiesToJoinCount`

Gets the number of entities that are joined to create a composite curve.
Gets the number of entities that are joined to create a composite curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEntitiesToJoinCount() As System.Integer
```

```

Dim instance As ICompositeCurveFeatureData
Dim value As System.Integer
 
value = instance.GetEntitiesToJoinCount()
```

```

System.int GetEntitiesToJoinCount()
```

```

System.int GetEntitiesToJoinCount(); 
```

#### Return Value

Number of entities

Remarks

Call this method before calling [ICompositeCurveFeatureData::IGetEntitiesToJoin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~IGetEntitiesToJoin.md).

Example

[Insert a Composite Curve (C#)](Insert_a_Composite_Curve_Example_CSharp.htm)  
[Insert a Composite Curve (VB.NET)](Insert_a_Composite_Curve_Example_VBNET.htm)  
[Insert a Composite Curve (VBA)](Insert_a_Composite_Curve_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICompositeCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData.md)  
[ICompositeCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData_members.md)  
[ICompositeCurveFeatureData::GetEntitiesToJoin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~GetEntitiesToJoin.md)

# SetPoints Method (IPrimaryMemberPointLengthFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~SetPoints`

Sets the vertexes, sketch points, and reference points.
Sets the vertexes, sketch points, and reference points.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetPoints( _
   ByVal Points As System.Object _
) As System.Boolean
```

```

Dim instance As IPrimaryMemberPointLengthFeatureData
Dim Points As System.Object
Dim value As System.Boolean
 
value = instance.SetPoints(Points)
```

```

System.bool SetPoints( 
   System.object Points
)
```

```

System.bool SetPoints( 
   System.Object^ Points
) 
```

#### Parameters

*Points*
:   Array of [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)es, [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)s, and/or [IRefPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.md)s

#### Return Value

True if points successfully set, false if not

Remarks

Use [IPrimaryMemberPointLengthFeatureData::UnChainPointsAndLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~UnChainPointsAndLength.md) to specify whether to chain link members along a chain of points.

Example

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryMemberPointLengthFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.md)  
[IPrimaryMemberPointLengthFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData_members.md)

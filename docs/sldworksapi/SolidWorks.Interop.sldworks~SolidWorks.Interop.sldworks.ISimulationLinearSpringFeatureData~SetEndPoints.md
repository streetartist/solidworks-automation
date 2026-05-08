# SetEndPoints Method (ISimulationLinearSpringFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData~SetEndPoints`

Obsolete. Superseded by ISimulationSpringFeatureData::SetEndPoints.
Obsolete. Superseded by [ISimulationSpringFeatureData::SetEndPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~SetEndPoints.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetEndPoints( _
   ByVal PDirDisp1 As System.Object, _
   ByVal PDirDisp2 As System.Object _
) 
```

```

Dim instance As ISimulationLinearSpringFeatureData
Dim PDirDisp1 As System.Object
Dim PDirDisp2 As System.Object
 
instance.SetEndPoints(PDirDisp1, PDirDisp2)
```

```

void SetEndPoints( 
   System.object PDirDisp1,
   System.object PDirDisp2
)
```

```

void SetEndPoints( 
   System.Object^ PDirDisp1,
   System.Object^ PDirDisp2
) 
```

#### Parameters

*PDirDisp1*
:   Linear edge, vertex, or sketch point

*PDirDisp2*
:   Linear edge, vertex, or sketch point

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationLinearSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData.md)  
[ISimulationLinearSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData_members.md)  
[ISimulationLinearspringFeatureData::GetEndPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData~GetEndPoints.md)

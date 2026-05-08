# SetEndPoints Method (ISimulationDamperFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData~SetEndPoints`

Sets the end points for this damper feature.
Sets the end points for this damper feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetEndPoints( _
   ByVal PDirDisp1 As System.Object, _
   ByVal PDirDisp2 As System.Object _
) As System.Boolean
```

```

Dim instance As ISimulationDamperFeatureData
Dim PDirDisp1 As System.Object
Dim PDirDisp2 As System.Object
Dim value As System.Boolean
 
value = instance.SetEndPoints(PDirDisp1, PDirDisp2)
```

```

System.bool SetEndPoints( 
   System.object PDirDisp1,
   System.object PDirDisp2
)
```

```

System.bool SetEndPoints( 
   System.Object^ PDirDisp1,
   System.Object^ PDirDisp2
) 
```

#### Parameters

*PDirDisp1*
:   Damper end point

*PDirDisp2*
:   Damper end point

#### Return Value

True if the operation succeeds, false if it fails

Example

See [ISimulationDamperFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationDamperFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData.md)  
[ISimulationDamperFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData_members.md)  
[ISimulationDamperFeatureData::GetEndPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData~GetEndPoints.md)

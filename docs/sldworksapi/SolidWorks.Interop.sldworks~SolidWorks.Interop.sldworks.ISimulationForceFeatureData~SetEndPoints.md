# SetEndPoints Method (ISimulationForceFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~SetEndPoints`

Sets the end points for this Force feature.
Sets the end points for this Force feature.

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

Dim instance As ISimulationForceFeatureData
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
:   Force end point

*PDirDisp2*
:   Force end point

#### Return Value

True if the operation succeeds, false if it fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.md)  
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.md)  
[ISimulationForceFeatureData::GetEndPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetEndPoints.md)

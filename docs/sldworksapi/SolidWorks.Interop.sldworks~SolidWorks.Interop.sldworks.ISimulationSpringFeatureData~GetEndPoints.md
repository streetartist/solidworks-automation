# GetEndPoints Method (ISimulationSpringFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~GetEndPoints`

Gets the end points for this simulation spring feature.
Gets the end points for this simulation spring feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEndPoints( _
   ByRef PDirDisp1 As System.Object, _
   ByRef PDirDisp2 As System.Object, _
   ByRef Type1 As System.Integer, _
   ByRef Type2 As System.Integer _
) As System.Boolean
```

```

Dim instance As ISimulationSpringFeatureData
Dim PDirDisp1 As System.Object
Dim PDirDisp2 As System.Object
Dim Type1 As System.Integer
Dim Type2 As System.Integer
Dim value As System.Boolean
 
value = instance.GetEndPoints(PDirDisp1, PDirDisp2, Type1, Type2)
```

```

System.bool GetEndPoints( 
   out System.object PDirDisp1,
   out System.object PDirDisp2,
   out System.int Type1,
   out System.int Type2
)
```

```

System.bool GetEndPoints( 
   [Out] System.Object^ PDirDisp1,
   [Out] System.Object^ PDirDisp2,
   [Out] System.int Type1,
   [Out] System.int Type2
) 
```

#### Parameters

*PDirDisp1*
:   Feature

*PDirDisp2*
:   Feature

*Type1*
:   Type of end point as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

*Type2*
:   Type of end point as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.md)  
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.md)  
[ISimulationSpringFeatureData::SetEndPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~SetEndPoints.md)

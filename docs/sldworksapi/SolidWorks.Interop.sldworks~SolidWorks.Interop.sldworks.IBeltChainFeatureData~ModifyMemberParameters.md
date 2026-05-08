# ModifyMemberParameters Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~ModifyMemberParameters`

Changes diameter and whether to flip the belt side of the specified pulley component.
Changes diameter and whether to flip the belt side of the specified pulley component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ModifyMemberParameters( _
   ByVal PulleyCompObject As System.Object, _
   ByVal Diameter As System.Double, _
   ByVal Flip As System.Boolean _
) As System.Boolean
```

```

Dim instance As IBeltChainFeatureData
Dim PulleyCompObject As System.Object
Dim Diameter As System.Double
Dim Flip As System.Boolean
Dim value As System.Boolean
 
value = instance.ModifyMemberParameters(PulleyCompObject, Diameter, Flip)
```

```

System.bool ModifyMemberParameters( 
   System.object PulleyCompObject,
   System.double Diameter,
   System.bool Flip
)
```

```

System.bool ModifyMemberParameters( 
   System.Object^ PulleyCompObject,
   System.double Diameter,
   System.bool Flip
) 
```

#### Parameters

*PulleyCompObject*
:   Pulley component

*Diameter*
:   Diameter > 0.0 to change; 0.0 to not change

*Flip*
:   True to flip the belt side, false to not

#### Return Value

True if pulley component successfully modifed, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md)  
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.md)

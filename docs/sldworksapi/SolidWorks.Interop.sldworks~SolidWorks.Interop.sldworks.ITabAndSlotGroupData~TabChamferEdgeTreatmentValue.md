# TabChamferEdgeTreatmentValue Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabChamferEdgeTreatmentValue`

Gets or sets the chamfer distance for tab edges.
Gets or sets the chamfer distance for tab edges.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TabChamferEdgeTreatmentValue As System.Double
```

```

Dim instance As ITabAndSlotGroupData
Dim value As System.Double
 
instance.TabChamferEdgeTreatmentValue = value
 
value = instance.TabChamferEdgeTreatmentValue
```

```

System.double TabChamferEdgeTreatmentValue {get; set;}
```

```

property System.double TabChamferEdgeTreatmentValue {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Chamfer distance

Remarks

This property is valid only if [ITabAndSlotGroupData::TabEdgesType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabEdgesType.md) is set to [swTabEdgesType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabEdgesType_e.html).ChamferEdge.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.md)  
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.md)

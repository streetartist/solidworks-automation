# TabFilletEdgeTreatmentValue Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabFilletEdgeTreatmentValue`

Gets or sets the fillet radius for tab edges.
Gets or sets the fillet radius for tab edges.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TabFilletEdgeTreatmentValue As System.Double
```

```

Dim instance As ITabAndSlotGroupData
Dim value As System.Double
 
instance.TabFilletEdgeTreatmentValue = value
 
value = instance.TabFilletEdgeTreatmentValue
```

```

System.double TabFilletEdgeTreatmentValue {get; set;}
```

```

property System.double TabFilletEdgeTreatmentValue {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Fillet radius

Remarks

This property is valid only if [ITabAndSlotGroupData::TabEdgesType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabEdgesType.md) is set to [swTabEdgesType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabEdgesType_e.html).FilletEdge.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.md)  
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.md)

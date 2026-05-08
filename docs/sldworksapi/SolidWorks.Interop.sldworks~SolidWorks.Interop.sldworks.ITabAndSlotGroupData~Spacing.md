# Spacing Property (ITabAndSlotGroupData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~Spacing`

Gets or sets the spacing between tabs/slots.
Gets or sets the spacing between tabs/slots.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Spacing As System.Double
```

```

Dim instance As ITabAndSlotGroupData
Dim value As System.Double
 
instance.Spacing = value
 
value = instance.Spacing
```

```

System.double Spacing {get; set;}
```

```

property System.double Spacing {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Spacing between tabs

Remarks

This property is valid only if [ITabAndSlotGroupData::SpacingType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SpacingType.md) is set to [swTabSlotFeatureSpacingType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabSlotFeatureSpacingType_e.html).SpacingLength.

The value of this property drives the number of instances.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.md)  
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.md)

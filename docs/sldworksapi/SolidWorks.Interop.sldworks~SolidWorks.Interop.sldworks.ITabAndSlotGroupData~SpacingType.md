# SpacingType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SpacingType`

Gets or sets the type of spacing of tabs/slots in this group.
Gets or sets the type of spacing of tabs/slots in this group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SpacingType As System.Integer
```

```

Dim instance As ITabAndSlotGroupData
Dim value As System.Integer
 
instance.SpacingType = value
 
value = instance.SpacingType
```

```

System.int SpacingType {get; set;}
```

```

property System.int SpacingType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Spacing type as defined in [swTabSlotFeatureSpacingType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabSlotFeatureSpacingType_e.html)

Example

See the [ITabAndSlotFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.md)  
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.md)

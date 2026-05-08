# SlotClearance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SlotClearance`

Gets or sets the offset of the slots relative to the tabs.
Gets or sets the offset of the slots relative to the tabs.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SlotClearance As System.Double
```

```

Dim instance As ITabAndSlotGroupData
Dim value As System.Double
 
instance.SlotClearance = value
 
value = instance.SlotClearance
```

```

System.double SlotClearance {get; set;}
```

```

property System.double SlotClearance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Slot clearance

Remarks

This property allows you to make the slots larger than the tabs.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.md)  
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.md)

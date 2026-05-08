# D1OffsetFromStart Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~D1OffsetFromStart`

Gets or sets the starting offset of the tabs/slots in this group.
Gets or sets the starting offset of the tabs/slots in this group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D1OffsetFromStart As System.Double
```

```

Dim instance As ITabAndSlotGroupData
Dim value As System.Double
 
instance.D1OffsetFromStart = value
 
value = instance.D1OffsetFromStart
```

```

System.double D1OffsetFromStart {get; set;}
```

```

property System.double D1OffsetFromStart {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Distance from the edge where to start the tabs and slots

Remarks

This method is valid only if [ITabAndSlotGroupData::Offset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~Offset.md) is set to true.

If you want the tabs/slots to span the entire edge of the model, set both this property and [ITabAndSlotGroupData::D2OffsetFromEnd](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~D2OffsetFromEnd.md) to zero.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.md)  
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.md)

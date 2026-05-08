# Offset Property (ITabAndSlotGroupData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~Offset`

Gets or sets whether to offset the tabs/slots from the edge of the model.
Gets or sets whether to offset the tabs/slots from the edge of the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Offset As System.Boolean
```

```

Dim instance As ITabAndSlotGroupData
Dim value As System.Boolean
 
instance.Offset = value
 
value = instance.Offset
```

```

System.bool Offset {get; set;}
```

```

property System.bool Offset {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to offset the tabs/slots, false to not

Remarks

If you set this property to true, also set:

- [ITabAndSlotGroupData::D1OffsetFromStart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~D1OffsetFromStart.md)
- [ITabAndSlotGroupData::D2OffsetFromEnd](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~D2OffsetFromEnd.md)

Example

See the [ITabAndSlotFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.md)  
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.md)

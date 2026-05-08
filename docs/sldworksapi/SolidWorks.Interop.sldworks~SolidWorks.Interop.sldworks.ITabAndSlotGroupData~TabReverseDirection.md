# TabReverseDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabReverseDirection`

Gets or sets whether to reverse the tab offset from surface value.
Gets or sets whether to reverse the tab offset from surface value.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TabReverseDirection As System.Boolean
```

```

Dim instance As ITabAndSlotGroupData
Dim value As System.Boolean
 
instance.TabReverseDirection = value
 
value = instance.TabReverseDirection
```

```

System.bool TabReverseDirection {get; set;}
```

```

property System.bool TabReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reverse the tab offset from surface value, false to not

Remarks

This property is valid only if valid only if [ITabAndSlotGroupData::TabHeightType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabHeightType.md) is set to [swTabSlotFeatureHeightType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabSlotFeatureHeightType_e.html).OffsetFromSurface.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.md)  
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.md)

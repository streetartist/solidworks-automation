# TabOffsetValue Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabOffsetValue`

Gets or sets the tab offset value.
Gets or sets the tab offset value.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TabOffsetValue As System.Double
```

```

Dim instance As ITabAndSlotGroupData
Dim value As System.Double
 
instance.TabOffsetValue = value
 
value = instance.TabOffsetValue
```

```

System.double TabOffsetValue {get; set;}
```

```

property System.double TabOffsetValue {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Tab offset value

Remarks

This property is:

- measured from [ITabAndSlotGroupData::SelectionSlotFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SelectionSlotFace.md)

    -and-

- valid only if [ITabAndSlotGroupData::TabHeightType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabHeightType.md) is set to [swTabSlotFeatureHeightType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabSlotFeatureHeightType_e.html).OffsetFromSurface.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.md)  
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.md)

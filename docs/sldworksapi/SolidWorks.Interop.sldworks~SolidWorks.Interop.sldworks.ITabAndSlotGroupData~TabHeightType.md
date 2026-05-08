# TabHeightType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabHeightType`

Gets or sets the type of tab height.
Gets or sets the type of tab height.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TabHeightType As System.Integer
```

```

Dim instance As ITabAndSlotGroupData
Dim value As System.Integer
 
instance.TabHeightType = value
 
value = instance.TabHeightType
```

```

System.int TabHeightType {get; set;}
```

```

property System.int TabHeightType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Tab height type as defined in [swTabSlotFeatureHeightType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabSlotFeatureHeightType_e.html)

Remarks

If you set this property to swTabSlotFeatureHeightType\_e:

- Blind, then use [ITabAndSlotGroupData::TabHeightValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabHeightValue.md) to set the tab height.
- OffsetFromSurface, then use [ITabAndSlotGroupData::TabOffsetValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabOffsetValue.md) to set the tab offset value as measured from the slot face. Also set [ITabAndSlotGroupData::TabReverseDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~TabReverseDirection.md).
- UpToSurface, then the tab height is automatically set to the distance up to the slot face.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.md)  
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.md)

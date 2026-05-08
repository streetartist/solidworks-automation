# SpacingNumberOfInstances Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SpacingNumberOfInstances`

Gets or sets the number of instances of equally spaced tabs/slots in this group.
Gets or sets the number of instances of equally spaced tabs/slots in this group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SpacingNumberOfInstances As System.Integer
```

```

Dim instance As ITabAndSlotGroupData
Dim value As System.Integer
 
instance.SpacingNumberOfInstances = value
 
value = instance.SpacingNumberOfInstances
```

```

System.int SpacingNumberOfInstances {get; set;}
```

```

property System.int SpacingNumberOfInstances {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Number of instances

Remarks

This property is valid only if [ITabAndSlotGroupData::SpacingType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData~SpacingType.md) is set to [swTabSlotFeatureSpacingType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabSlotFeatureSpacingType_e.html).EqualSpacing.

Example

See the [ITabAndSlotFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITabAndSlotGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData.md)  
[ITabAndSlotGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.md)

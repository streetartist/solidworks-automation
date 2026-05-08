# OffsetReverseDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~OffsetReverseDirection`

Gets or sets whether to reverse the offset direction for this Advanced Hole element.
Gets or sets whether to reverse the offset direction for this Advanced Hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OffsetReverseDirection As System.Boolean
```

```

Dim instance As IAdvancedHoleElementData
Dim value As System.Boolean
 
instance.OffsetReverseDirection = value
 
value = instance.OffsetReverseDirection
```

```

System.bool OffsetReverseDirection {get; set;}
```

```

property System.bool OffsetReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reverse the offset direction, false to not

Remarks

This property is valid only when [IAdvancedHoleElementData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~EndCondition.md) is set to [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html).swEndCondOffsetFromSurface.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedHoleElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.md)  
[IAdvancedHoleElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.md)  
[IAdvancedHoleElementData::OffsetDistance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~OffsetDistance.md)

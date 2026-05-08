# UseStandardDepth Property (ITaperedTapElementData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData~UseStandardDepth`

Gets or sets whether to use the standard offset distance for the end condition of this tapered tap hole element.
Gets or sets whether to use the standard offset distance for the end condition of this tapered tap hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseStandardDepth As System.Boolean
```

```

Dim instance As ITaperedTapElementData
Dim value As System.Boolean
 
instance.UseStandardDepth = value
 
value = instance.UseStandardDepth
```

```

System.bool UseStandardDepth {get; set;}
```

```

property System.bool UseStandardDepth {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use the standard offset distance, false to not (see **Remarks**)

Remarks

This property is valid only if [IAdvancedHoleFeatureData::UseBaselineDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~UseBaselineDimensions.md) is set to true.

If this property is set to false, then use [IAdvancedHoleElementData::OffsetDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~OffsetDistance.md) to set the custom offset distance.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITaperedTapElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData.md)  
[ITaperedTapElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData_members.md)  
[IAdvancedHoleElementData::OffsetReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~OffsetReverseDirection.md)

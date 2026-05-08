# UseThicknessRatioForOffset Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~UseThicknessRatioForOffset`

Gets or sets whether a ratio of the thickness is used to specify the offset for this end-cap feature.
Gets or sets whether a ratio of the thickness is used to specify the offset for this end-cap feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseThicknessRatioForOffset As System.Boolean
```

```

Dim instance As IEndCapFeatureData
Dim value As System.Boolean
 
instance.UseThicknessRatioForOffset = value
 
value = instance.UseThicknessRatioForOffset
```

```

System.bool UseThicknessRatioForOffset {get; set;}
```

```

property System.bool UseThicknessRatioForOffset {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use a ratio of the thickness, false to not

Remarks

|  |  |
| --- | --- |
| **If this property is set to...** | **Then you can use...** |
| True | [IEndCapFeatureData::ThicknessRatioForOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~ThicknessRatioForOffset.md) to set the offset distance of the end cap as a ratio of the thickness of the structural member being capped. |
| False | [IEndCapFeatureData::OffsetDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~OffsetDistance.md) to set the offset distance for this end-cap feature. |

Example

See the [IEndCapFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.md)  
[IEndCapFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.md)  
[IEndCapFeatureData::Thickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~Thickness.md)

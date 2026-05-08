# UseReliefRatio Property (ISweptFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseReliefRatio`

Gets or sets whether to use the relief ratio in this swept flange feature.
Gets or sets whether to use the relief ratio in this swept flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseReliefRatio As System.Boolean
```

```

Dim instance As ISweptFlangeFeatureData
Dim value As System.Boolean
 
instance.UseReliefRatio = value
 
value = instance.UseReliefRatio
```

```

System.bool UseReliefRatio {get; set;}
```

```

property System.bool UseReliefRatio {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use the relief ratio, false to not

Remarks

This property is valid:

- If [ISweptFlangeFeatureData::UseDefaultBendRelief](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseDefaultBendRelief.md) is false,

   - and -

- For regular swept flanges, but for cylindrical/conical swept flanges only during creation,

   - and -

- When [ISweptFlangeFeatureData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~ReliefType.md) is [swSheetMetalReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefRectangular or swSheetMetalReliefTypes\_e.swSheetMetalReliefObround.

If this property is:

- True, then use [ISweptFlangeFeatureData::ReliefRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~ReliefRatio.md) to set a ratio of bend relief width to bend relief depth.
- False, then specify [ISweptFlangeFeatureData::ReliefWidth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~ReliefWidth.md) and [ISweptFlangeFeatureData::ReliefDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~ReliefDepth.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md)  
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.md)

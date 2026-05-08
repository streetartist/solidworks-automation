# ReliefRatio Property (ISweptFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~ReliefRatio`

Gets or sets the bend relief ratio for this swept flange feature.
Gets or sets the bend relief ratio for this swept flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReliefRatio As System.Double
```

```

Dim instance As ISweptFlangeFeatureData
Dim value As System.Double
 
instance.ReliefRatio = value
 
value = instance.ReliefRatio
```

```

System.double ReliefRatio {get; set;}
```

```

property System.double ReliefRatio {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Ratio of bend relief width to bend relief depth

Remarks

This property is valid:

- For regular swept flanges, but for cylindrical or conical swept flanges only during creation,
- When [ISweptFlangeFeatureData::UseReliefRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseReliefRatio.md) is true,

    - and -

- When [ISweptFlangeFeatureData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~ReliefType.md) is [swSheetMetalReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefRectangular or swSheetMetalReliefTypes\_e.swSheetMetalReliefObround.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md)  
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.md)

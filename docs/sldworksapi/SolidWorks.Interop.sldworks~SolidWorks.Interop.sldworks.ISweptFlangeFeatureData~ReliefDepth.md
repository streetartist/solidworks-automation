# ReliefDepth Property (ISweptFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~ReliefDepth`

Gets or sets the bend relief depth for this swept flange feature.
Gets or sets the bend relief depth for this swept flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReliefDepth As System.Double
```

```

Dim instance As ISweptFlangeFeatureData
Dim value As System.Double
 
instance.ReliefDepth = value
 
value = instance.ReliefDepth
```

```

System.double ReliefDepth {get; set;}
```

```

property System.double ReliefDepth {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Bend relief depth

Remarks

This property is valid:

- If [ISweptFlangeFeatureData::UseReliefRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseReliefRatio.md) is false,

    - and -

- For regular swept flanges, but for cylindrical or conical swept flanges only during creation,

    - and -

- When [ISweptFlangeFeatureData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~ReliefType.md) is [swSheetMetalReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSheetMetalReliefTypes_e.html).swSheetMetalReliefRectangular or swSheetMetalReliefTypes\_e.swSheetMetalReliefObround.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md)  
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.md)

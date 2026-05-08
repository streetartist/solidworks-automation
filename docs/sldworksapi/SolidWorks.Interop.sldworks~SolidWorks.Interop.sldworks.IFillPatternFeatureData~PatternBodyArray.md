# PatternBodyArray Property (IFillPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternBodyArray`

Gets or sets the array of bodies to pattern in this fill pattern feature.
Gets or sets the array of bodies to pattern in this fill pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PatternBodyArray As System.Object
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Object
 
instance.PatternBodyArray = value
 
value = instance.PatternBodyArray
```

```

System.object PatternBodyArray {get; set;}
```

```

property System.Object^ PatternBodyArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)s to pattern

Remarks

This property is valid only if [IFillPatternFeatureData::PatternElement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternElement.md) is [swPatternElementSelection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternElementSelection_e.html).swBodiesToPattern.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md)  
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.md)

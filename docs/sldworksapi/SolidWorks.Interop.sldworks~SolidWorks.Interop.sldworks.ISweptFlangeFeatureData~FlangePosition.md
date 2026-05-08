# FlangePosition Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~FlangePosition`

Gets or sets the flange position of this swept flange feature.
Gets or sets the flange position of this swept flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FlangePosition As System.Integer
```

```

Dim instance As ISweptFlangeFeatureData
Dim value As System.Integer
 
instance.FlangePosition = value
 
value = instance.FlangePosition
```

```

System.int FlangePosition {get; set;}
```

```

property System.int FlangePosition {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Flange position as defined by [swSweptFlangePostionTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFlangePositionTypes_e.html)

Example

See the [ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md)  
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.md)

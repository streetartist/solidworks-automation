# CornerDefaults Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~CornerDefaults`

Gets or sets the sheet metal corner type in this convert solid feature.
Gets or sets the sheet metal corner type in this convert solid feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CornerDefaults As System.Integer
```

```

Dim instance As IConvertSolidFeatureData
Dim value As System.Integer
 
instance.CornerDefaults = value
 
value = instance.CornerDefaults
```

```

System.int CornerDefaults {get; set;}
```

```

property System.int CornerDefaults {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Sheet metal corner type as defined by [swSheetMetalOverlapTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSheetMetalOverlapTypes_e.html)

Example

See the [IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md)  
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.md)

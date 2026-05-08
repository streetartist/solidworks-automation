# RipOverlapRatio Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~RipOverlapRatio`

Gets or sets the default ratio for all overlap and underlap rips in this convert solid feature.
Gets or sets the default ratio for all overlap and underlap rips in this convert solid feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RipOverlapRatio As System.Double
```

```

Dim instance As IConvertSolidFeatureData
Dim value As System.Double
 
instance.RipOverlapRatio = value
 
value = instance.RipOverlapRatio
```

```

System.double RipOverlapRatio {get; set;}
```

```

property System.double RipOverlapRatio {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Default ratio for overlap and underlap rips; 0.0 <= Rip overlap ratio <= 1.0

Example

See the [IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md)  
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.md)

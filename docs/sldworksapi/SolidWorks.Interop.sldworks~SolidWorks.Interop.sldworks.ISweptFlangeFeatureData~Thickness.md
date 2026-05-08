# Thickness Property (ISweptFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Thickness`

Gets or sets the sheet metal thickness of this swept flange feature.
Gets or sets the sheet metal thickness of this swept flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Thickness As System.Double
```

```

Dim instance As ISweptFlangeFeatureData
Dim value As System.Double
 
instance.Thickness = value
 
value = instance.Thickness
```

```

System.double Thickness {get; set;}
```

```

property System.double Thickness {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Sheet metal thickness

Remarks

This property is valid only when not creating the swept flange on an existing sheet metal feature.

The setter of this property is valid only if [ISweptFlangeFeatureData::OverrideDefaultSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~OverrideDefaultSheetMetalParameters.md) is true.

This property gets:

- Default thickness if ISweptFlangeFeatureData::OverrideDefaultSheetMetalParameters is false.

- Custom thickness if ISweptFlangeFeatureData::OverrideDefaultSheetMetalParameters is true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md)  
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.md)

# GaugeTableFile Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~GaugeTableFile`

Gets or sets the gauge table file in this convert solid feature.
Gets or sets the gauge table file in this convert solid feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GaugeTableFile As System.String
```

```

Dim instance As IConvertSolidFeatureData
Dim value As System.String
 
instance.GaugeTableFile = value
 
value = instance.GaugeTableFile
```

```

System.string GaugeTableFile {get; set;}
```

```

property System.String^ GaugeTableFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Pathname of gauge table file

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md)  
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.md)

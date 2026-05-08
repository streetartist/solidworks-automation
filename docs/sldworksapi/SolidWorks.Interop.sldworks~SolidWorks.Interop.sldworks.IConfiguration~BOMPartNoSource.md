# BOMPartNoSource Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~BOMPartNoSource`

Gets or sets the source of the part number used in the BOM table.
Gets or sets the source of the part number used in the BOM table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BOMPartNoSource As System.Integer
```

```

Dim instance As IConfiguration
Dim value As System.Integer
 
instance.BOMPartNoSource = value
 
value = instance.BOMPartNoSource
```

```

System.int BOMPartNoSource {get; set;}
```

```

property System.int BOMPartNoSource {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Source of part number as defined in [swBOMPartNumberSource\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMPartNumberSource_e.html)

Remarks

If you specify this property with anything other than swBOMPartNumberSource\_e.swBOMPartNumber\_UserSpecified, then [IConfiguration::AlternateName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AlternateName.md) is set to an empty string.

Example

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::Name Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Name.md)  
[IConfiguration::UseAlternateNameInBOM Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UseAlternateNameInBOM.md)

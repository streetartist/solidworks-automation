# UseDescriptionInBOM Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UseDescriptionInBOM`

Gets or sets whether the description of the configuration is displayed in the bill of materials.
Gets or sets whether the [description](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Description.md) of the configuration is displayed in the bill of materials.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseDescriptionInBOM As System.Boolean
```

```

Dim instance As IConfiguration
Dim value As System.Boolean
 
instance.UseDescriptionInBOM = value
 
value = instance.UseDescriptionInBOM
```

```

System.bool UseDescriptionInBOM {get; set;}
```

```

property System.bool UseDescriptionInBOM {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True displays the description of the configuration in the bill of materials, false does not

Example

[Display Configuration Description in Bill of Materials (C#)](Display_Configuration_Description_in_Bill_of_Materials_Example_CSharp.htm)  
[Display Configuration Description in Bill of Materials (VB.NET)](Display_Configuration_Description_in_Bill_of_Materials_Example_VBNET.htm)  
[Display Configuration Description in Bill of Materials (VBA)](Display_Configuration_Description_in_Bill_of_Materials_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)

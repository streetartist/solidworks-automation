# Description Property (IConfiguration)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Description`

Gets or sets the description of the configuration.
Gets or sets the description of the configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Description As System.String
```

```

Dim instance As IConfiguration
Dim value As System.String
 
instance.Description = value
 
value = instance.Description
```

```

System.string Description {get; set;}
```

```

property System.String^ Description {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Description of the configuration

Example

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)  
[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)  
[Display Configuration Description in Bill of Materials (C#)](Display_Configuration_Description_in_Bill_of_Materials_Example_CSharp.htm)  
[Display Configuration Description in Bill of Materials (VB.NET)](Display_Configuration_Description_in_Bill_of_Materials_Example_VBNET.htm)  
[Display Configuration Description in Bill of Materials (VBA)](Display_Configuration_Description_in_Bill_of_Materials_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::UseDescriptionInBOM Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UseDescriptionInBOM.md)

# AlternateName Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AlternateName`

Gets or sets the configuration's alternate name (i.e., user-specified name).
Gets or sets the configuration's alternate name (i.e., user-specified name).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AlternateName As System.String
```

```

Dim instance As IConfiguration
Dim value As System.String
 
instance.AlternateName = value
 
value = instance.AlternateName
```

```

System.string AlternateName {get; set;}
```

```

property System.String^ AlternateName {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Alternate or user-specified name for the configuration

Remarks

To display the configuration's alternate name as the part number in the bill of materials, use [IConfiguration::UseAlternateNameInBOM](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UseAlternateNameInBOM.md).

Configuration names must not contain any special characters reserved by SOLIDWORKS.

If you specify [IConfiguration::BOMPartNoSource](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~BOMPartNoSource.md) with anything other than [swBOMPartNumberSource\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBOMPartNumberSource_e.html).swBOMPartNumber\_UserSpecified, then this property is set to an empty string.

Example

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)  
[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)  
[Get List of Configurations (C#)](Get_List_Of_Configurations_Example_CSharp.htm)  
[Get List of Configurations (VB.NET)](Get_List_Of_Configurations_Example_VBNET.htm)  
[Get List of Configurations (VBA)](Get_List_Of_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)  
[IConfiguration::Name Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Name.md)

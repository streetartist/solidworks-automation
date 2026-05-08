# UseAlternateNameInBOM Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UseAlternateNameInBOM`

Gets or sets whether the alternate name (i.e., user-specified name) is displayed in the bill of materials for this configuration.
Gets or sets whether the [alternate name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AlternateName.md) (i.e., user-specified name) is displayed in the bill of materials for this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseAlternateNameInBOM As System.Boolean
```

```

Dim instance As IConfiguration
Dim value As System.Boolean
 
instance.UseAlternateNameInBOM = value
 
value = instance.UseAlternateNameInBOM
```

```

System.bool UseAlternateNameInBOM {get; set;}
```

```

property System.bool UseAlternateNameInBOM {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True displays the alternate name in the bill of materials, false does not

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

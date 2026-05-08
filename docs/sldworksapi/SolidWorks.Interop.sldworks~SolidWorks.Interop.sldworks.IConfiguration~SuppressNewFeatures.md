# SuppressNewFeatures Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SuppressNewFeatures`

Gets or sets whether to suppress new features in this configuration.
Gets or sets whether to suppress new features in this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SuppressNewFeatures As System.Boolean
```

```

Dim instance As IConfiguration
Dim value As System.Boolean
 
instance.SuppressNewFeatures = value
 
value = instance.SuppressNewFeatures
```

```

System.bool SuppressNewFeatures {get; set;}
```

```

property System.bool SuppressNewFeatures {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True suppresses the new feature in this configuration, false does not

Remarks

This setting applies only to inactive configurations. This property applies to new mates and features for assembly configurations.

Example

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)  
[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)

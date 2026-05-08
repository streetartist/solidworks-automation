# ShowChildComponentsInBOM Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ShowChildComponentsInBOM`

Obsolete. Superseded by IConfiguration::ChildComponentDisplayInBOM.
Obsolete. Superseded by [IConfiguration::ChildComponentDisplayInBOM.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ChildComponentDisplayInBOM.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowChildComponentsInBOM As System.Boolean
```

```

Dim instance As IConfiguration
Dim value As System.Boolean
 
instance.ShowChildComponentsInBOM = value
 
value = instance.ShowChildComponentsInBOM
```

```

System.bool ShowChildComponentsInBOM {get; set;}
```

```

property System.bool ShowChildComponentsInBOM {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True displays child components in a BOM, false does not

Remarks

This property applies only to assembly configurations. SOLIDWORKS always returns false when you get this property on a part configuration. Setting this property on a part configuration has no effect.

How the components appear in the report is mainly controlled by the display format of a BOM. However, this property does affect the output format. Specifically, if this property is set to false, the report includes only the subassembly, not the component parts of this model configuration (even if the BOM report requests that all parts be displayed).

Example

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)  
[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)

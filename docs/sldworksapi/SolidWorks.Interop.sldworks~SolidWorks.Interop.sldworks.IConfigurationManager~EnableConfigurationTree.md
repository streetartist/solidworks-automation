# EnableConfigurationTree Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~EnableConfigurationTree`

Gets or sets whether to update the ConfigurationManager tree.
Gets or sets whether to update the ConfigurationManager tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnableConfigurationTree As System.Boolean
```

```

Dim instance As IConfigurationManager
Dim value As System.Boolean
 
instance.EnableConfigurationTree = value
 
value = instance.EnableConfigurationTree
```

```

System.bool EnableConfigurationTree {get; set;}
```

```

property System.bool EnableConfigurationTree {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to update the ConfigurationManager tree, false to not (see Remarks)

Remarks

This property is set to true by default. Setting this property to false will increase the performance of SOLIDWORKS when performing multiple operations that affect the ConfigurationManager tree, such as deleting configurations. However, set this property back to true after performing such operations so that the ConfigurationManager tree will update thereafter.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.md)  
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.md)

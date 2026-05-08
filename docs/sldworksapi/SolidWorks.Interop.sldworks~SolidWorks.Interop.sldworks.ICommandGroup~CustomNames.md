# CustomNames Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~CustomNames`

Gets or sets the custom names in the CommandGroup.
Gets or sets the custom names in the CommandGroup.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CustomNames As System.String
```

```

Dim instance As ICommandGroup
Dim value As System.String
 
instance.CustomNames = value
 
value = instance.CustomNames
```

```

System.string CustomNames {get; set;}
```

```

property System.String^ CustomNames {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

String containing the custom names in the CommandGroup (see **Remarks**)

Remarks

Format CustomNames as a semicolon-separated list of the names of the custom feature types.

This method is applicable only if[ICommandGruop::SelectType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SelectType.md) is a custom feature type, like swSelATTRIBUTES. For example, if you want a context-sensitive, pop-up menu to appear for an attribute when the user right-clicks the attribute in the FeatureManager design tree, then:

1. Create the attribute (see [IAttributeDef::CreateInstance5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance5.md))
2. Set the name of the attribute in [ICommandGroup::SelectType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SelectType.md).
3. Set the name of the attribute definition in ICommandGroup::CustomNames.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)  
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.md)  
[ICommandManager::AddContextMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddContextMenu.md)

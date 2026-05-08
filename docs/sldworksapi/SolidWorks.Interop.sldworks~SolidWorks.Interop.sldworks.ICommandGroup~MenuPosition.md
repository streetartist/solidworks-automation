# MenuPosition Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~MenuPosition`

Gets or sets the position of the CommandGroup for the specified document templates.
Gets or sets the position of the CommandGroup for the specified document templates.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MenuPosition( _
   ByVal Context As System.Integer _
) As System.Integer
```

```

Dim instance As ICommandGroup
Dim Context As System.Integer
Dim value As System.Integer
 
instance.MenuPosition(Context) = value
 
value = instance.MenuPosition(Context)
```

```

System.int MenuPosition( 
   System.int Context
) {get; set;}
```

```

property System.int MenuPosition {
   System.int get(System.int Context);
   void set (System.int Context, System.int value);
}
```

#### Parameters

*Context*
:   Context as defined in [swDocTemplateTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocTemplateTypes_e.html)

#### Property Value

Position of the CommandGroup in the CommandManager

**NOTE:** Specify 0 to add the CommandGroup to the beginning of the CommandMananger, or specify -1 to add it to the end of the CommandManager.

Remarks

If setting the position of the CommandGroup using this property, you must use it before using [ICommandGroup::Activate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~Activate.md). If you use this property after using ICommandGroup::Activate, then this property has no effect.

If you do not use this property to set the position of the ICommandGroup, then the position specified in [ICommandManager::CreateCommandGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateCommandGroup.md) is used.

Calling this property to get the position of the CommandGroup returns the position of the CommandGroup set by either this property or ICommandManager::CreateCommandGroup.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)  
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.md)  
[ICommandGroup::HasMenu Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasMenu.md)

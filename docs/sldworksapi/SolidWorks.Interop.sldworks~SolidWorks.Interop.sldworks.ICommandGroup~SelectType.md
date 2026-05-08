# SelectType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SelectType`

This property:
This property:

- gets the type of object selected on the context sensitive, pop-up menu.
- sets the type of object that the user must select to show the context sensitive, pop-up menu.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SelectType As System.Integer
```

```

Dim instance As ICommandGroup
Dim value As System.Integer
 
instance.SelectType = value
 
value = instance.SelectType
```

```

System.int SelectType {get; set;}
```

```

property System.int SelectType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of object as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

Remarks

This property only applies to CommandGroups created using [ICommandManager::AddContextMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddContextMenu.md).

If setting SelectType to a custom feature type such as an attribute (swSelATTRIBUTES),  
then you must use [ICommandGroup::CustomNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~CustomNames.md) to set the name of the attribute definition.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)  
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.md)

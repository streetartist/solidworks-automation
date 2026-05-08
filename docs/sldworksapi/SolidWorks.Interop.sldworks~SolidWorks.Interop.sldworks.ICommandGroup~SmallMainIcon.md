# SmallMainIcon Property (ICommandGroup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SmallMainIcon`

Obsolete. Superseded by ICommandGroup::MainIconList.
Obsolete. Superseded by [ICommandGroup::MainIconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~MainIconList.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SmallMainIcon As System.String
```

```

Dim instance As ICommandGroup
Dim value As System.String
 
instance.SmallMainIcon = value
 
value = instance.SmallMainIcon
```

```

System.string SmallMainIcon {get; set;}
```

```

property System.String^ SmallMainIcon {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Path of the small bitmap or PNG for this CommandGroup

Remarks

The small bitmap must be 16x16 and use a 256-color palette.

Example

[Create Submenus in the CommandManager (C#)](Create_Submenus_in_the_CommandManager_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)  
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.md)  
[ICommandGroup::AddCommandItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddCommandItem2.md)  
[ICommandGroup::LargeIconList Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~LargeIconList.md)  
[ICommandGroup::LargeMainIcon Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~LargeMainIcon.md)  
[ICommandGroup::SmallIconList Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SmallIconList.md)

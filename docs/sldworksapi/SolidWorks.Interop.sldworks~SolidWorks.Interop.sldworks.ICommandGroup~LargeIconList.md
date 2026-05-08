# LargeIconList Property (ICommandGroup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~LargeIconList`

Obsolete. Superseded by ICommandGroup::IconList.
Obsolete. Superseded by [ICommandGroup::IconList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~IconList.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LargeIconList As System.String
```

```

Dim instance As ICommandGroup
Dim value As System.String
 
instance.LargeIconList = value
 
value = instance.LargeIconList
```

```

System.string LargeIconList {get; set;}
```

```

property System.String^ LargeIconList {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Path for the bitmap or PNG files containing all of the large images of the toolbar buttons and separators for this CommandGroup

Remarks

The bitmap or PNG file should contain all of the images for all of the large buttons and separators for this CommandGroup, in a single bitmap for both parent and child toolbars. Each image of each button must be 24x24. The images should use a 256-color palette.

You can only set this property for the top-level CommandGroup.

Example

[Create Submenus in the CommandManager (C#)](Create_Submenus_in_the_CommandManager_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)  
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.md)  
[ICommandGroup::AddCommandItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddCommandItem2.md)  
[ICommandGroup::LargeMainIcon Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~LargeMainIcon.md)  
[ICommandGroup::SmallIconList Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SmallIconList.md)  
[ICommandGroup::SmallMainIcon Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SmallMainIcon.md)

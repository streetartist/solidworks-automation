# MenuPinned Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~MenuPinned`

Gets or sets whether the SOLIDWORKS main menu is pinned.
Gets or sets whether the SOLIDWORKS main menu is pinned.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MenuPinned As System.Boolean
```

```

Dim instance As IFrame
Dim value As System.Boolean
 
instance.MenuPinned = value
 
value = instance.MenuPinned
```

```

System.bool MenuPinned {get; set;}
```

```

property System.bool MenuPinned {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to pin the SOLIDWORKS main menu, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.md)  
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.md)

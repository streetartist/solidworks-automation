# SetToolbarVisibility Method (ICommandGroup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SetToolbarVisibility`

Sets the visibility of the toolbar in the CommandGroup.
Sets the visibility of the toolbar in the CommandGroup.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetToolbarVisibility( _
   ByVal Visible As System.Boolean, _
   ByVal Mask As System.Integer _
) 
```

```

Dim instance As ICommandGroup
Dim Visible As System.Boolean
Dim Mask As System.Integer
 
instance.SetToolbarVisibility(Visible, Mask)
```

```

void SetToolbarVisibility( 
   System.bool Visible,
   System.int Mask
)
```

```

void SetToolbarVisibility( 
   System.bool Visible,
   System.int Mask
) 
```

#### Parameters

*Visible*
:   True to show the toolbar, false to hide it

*Mask*
:   Context in which to show or hide toolbar as defined in [swDocTemplateTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocTemplateTypes_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)  
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.md)  
[ICommandGroup::HasMenu Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasMenu.md)  
[ICommandGroup::HasToolbar Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasToolbar.md)  
[ICommandManager::AddContextMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddContextMenu.md)

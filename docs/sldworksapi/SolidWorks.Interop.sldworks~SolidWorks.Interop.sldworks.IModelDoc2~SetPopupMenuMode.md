# SetPopupMenuMode Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetPopupMenuMode`

Sets the pop-up menu mode.
Sets the pop-up menu mode.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetPopupMenuMode( _
   ByVal ModeIn As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim ModeIn As System.Integer
 
instance.SetPopupMenuMode(ModeIn)
```

```

void SetPopupMenuMode( 
   System.int ModeIn
)
```

```

void SetPopupMenuMode( 
   System.int ModeIn
) 
```

#### Parameters

*ModeIn*
:   Pop-up menu mode (see **Remarks**)

Remarks

When end users press the right-mouse button on an entity in the graphics window, they are be presented with one of two menu sets. These menu sets are defined as mode 0 and mode 1.

**Mode**

- 0 - Default shortcut mode. This mode presents the end user with options to Select Other, manipulate the view, access the properties dialog of the selected item, and so on.
- 1 - The end-user is presented with a limited set of choices including Select Other and Clear Selection. This mode is typically seen when a SOLIDWORKS dialog is active and the user is restricted to entity selection.

Using this method, you can simulate the same shortcut menu behavior as in the SOLIDWORKS user interface. If you have a dialog that requires user selection of entities, you can set the pop-up menu mode to 1 to simulate SOLIDWORKS behavior. Your application should always set the menu mode back to its previous value. To determine the previous behavior, call [IModelDoc2::GetPopupMenuMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPopupMenuMode.md) prior to calling to this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)

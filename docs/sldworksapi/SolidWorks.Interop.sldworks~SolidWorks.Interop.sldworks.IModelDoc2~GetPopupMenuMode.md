# GetPopupMenuMode Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPopupMenuMode`

Gets the current pop-up menu mode.
Gets the current pop-up menu mode.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPopupMenuMode() As System.Integer
```

```

Dim instance As IModelDoc2
Dim value As System.Integer
 
value = instance.GetPopupMenuMode()
```

```

System.int GetPopupMenuMode()
```

```

System.int GetPopupMenuMode(); 
```

#### Return Value

Current pop-up menu mode:

- 0 - Default shortcut mode. This presents end users with options to **Select Other**, manipulate the view, access the properties dialog of the selected item, and so on.
- 1 - End users are presented with a limited set of choices including **Select Other** and **Clear Selection**. This mode is typically seen when a SOLIDWORKS dialog is active and the end user is restricted to entity selection.

Remarks

When end users click the right-mouse button when the pointer is on an entity in the graphics window, they are presented with one of two distinct menu sets. These menu sets have been defined as mode 0 and mode 1.

Using [IModelDoc2::SetPopupMenuMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetPopupMenuMode.md), your application can simulate the same shortcut menu behavior as in the SOLIDWORKS user interface. If you have a dialog that requires end-user selection of entities, you can set the pop-up menu mode to 1 to simulate SOLIDWORKS behavior. Your application should always set the menu mode back to its previous value. You can determine the previous value by calling the IModelDoc2::GetPopupMenuMode before calling IModelDoc2::SetPopupMenuMode.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)

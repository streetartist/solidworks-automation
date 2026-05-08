# GetLightId Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILightDialog~GetLightId`

Gets the ID of the edited light in the light dialog.
Gets the ID of the edited light in the light dialog.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLightId() As System.Integer
```

```

Dim instance As ILightDialog
Dim value As System.Integer
 
value = instance.GetLightId()
```

```

System.int GetLightId()
```

```

System.int GetLightId(); 
```

#### Return Value

ID of the light currently being modified by the dialog; -1 if the light cannot be found

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILightDialog Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILightDialog.md)  
[ILightDialog Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILightDialog_members.md)

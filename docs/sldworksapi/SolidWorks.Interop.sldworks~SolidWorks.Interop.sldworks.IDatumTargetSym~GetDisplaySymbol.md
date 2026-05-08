# GetDisplaySymbol Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDisplaySymbol`

Gets whether the datum target symbol is displayed.
Gets whether the datum target symbol is displayed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDisplaySymbol() As System.Boolean
```

```

Dim instance As IDatumTargetSym
Dim value As System.Boolean
 
value = instance.GetDisplaySymbol()
```

```

System.bool GetDisplaySymbol()
```

```

System.bool GetDisplaySymbol(); 
```

#### Return Value

True if the datum target symbol is displayed, false if it is not

Remarks

Use:

- [IDatumTargetSym::GetDisplayTargetArea](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDisplayTargetArea.md) to determine whether the datum target area part of this annotation is displayed.
- [IDatumTargetSym::SetDisplay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDisplay.md) to enable or disable the display of the target area or symbol.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.md)  
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.md)  
[IDatumTargetSym::GetDisplaySizeOutside Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDisplaySizeOutside.md)  
[IDatumTargetSym::GetDisplaySizeOutside Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDisplaySizeOutside.md)  
[IDatumTargetSym::SetDisplay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDisplay.md)  
[IDatumTargetSym::SetDisplay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDisplay.md)

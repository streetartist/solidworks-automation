# GetTargetShape Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTargetShape`

Gets the shape or style of the datum target area.
Gets the shape or style of the datum target area.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTargetShape() As System.Integer
```

```

Dim instance As IDatumTargetSym
Dim value As System.Integer
 
value = instance.GetTargetShape()
```

```

System.int GetTargetShape()
```

```

System.int GetTargetShape(); 
```

#### Return Value

Target area shape or style as defined in [swDatumTargetAreaShape\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDatumTargetAreaShape_e.html)

Remarks

Use [IDatumTargetSym::SetTargetArea](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetTargetArea.md) to set the shape of the target area.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.md)  
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.md)  
[IDatumTargetSym::GetDisplayTargetArea Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDisplayTargetArea.md)  
[IDatumTargetSym::GetTargetAreaSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetTargetAreaSize.md)  
[IDatumTargetSym::SetTargetArea Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetTargetArea.md)

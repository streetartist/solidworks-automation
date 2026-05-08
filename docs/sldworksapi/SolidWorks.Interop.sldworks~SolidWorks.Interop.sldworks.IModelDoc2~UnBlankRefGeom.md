# UnBlankRefGeom Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~UnBlankRefGeom`

Shows the selected, hidden reference geometry in the graphics window.
Shows the selected, hidden reference geometry in the graphics window.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub UnBlankRefGeom() 
```

```

Dim instance As IModelDoc2
 
instance.UnBlankRefGeom()
```

```

void UnBlankRefGeom()
```

```

void UnBlankRefGeom(); 
```

Remarks

If you select a reference plane and call this method, then the plane will be visible in the graphics area. This method has the same effect as selecting an item and choosing Show on the shortcut menu.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::BlankRefGeom Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~BlankRefGeom.md)

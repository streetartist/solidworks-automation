# BlankRefGeom Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~BlankRefGeom`

Hides the selected reference geometry in the graphics window.
Hides the selected reference geometry in the graphics window.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub BlankRefGeom() 
```

```

Dim instance As IModelDoc2
 
instance.BlankRefGeom()
```

```

void BlankRefGeom()
```

```

void BlankRefGeom(); 
```

Remarks

If you select a reference plane and then call this method, the plane is invisible in the graphics area. This method has the same effect as right-clicking an item and selecting **Hide** on the shortcut menu.

Example

[Create Replace Face Feature (C#)](Replace_Face_Example_CSharp.htm)  
[Create Replace Face Feature (VB.NET)](Replace_Face_Example_VBNET.htm)  
[Create Replace Face Feature (VBA)](Replace_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::UnBlankRefGeom Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~UnBlankRefGeom.md)

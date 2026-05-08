# SetLineColor Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetLineColor`

Sets the color for the lines in the part document.
Sets the color for the lines in the part document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetLineColor( _
   ByVal Color As System.Integer _
) 
```

```

Dim instance As IPartDoc
Dim Color As System.Integer
 
instance.SetLineColor(Color)
```

```

void SetLineColor( 
   System.int Color
)
```

```

void SetLineColor( 
   System.int Color
) 
```

#### Parameters

*Color*
:   Color definition as a COLORREF

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::SetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetLineStyle.md)  
[IPartDoc::SetLineWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetLineWidth.md)

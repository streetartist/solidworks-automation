# InsertDome Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertDome`

Obsolete. Superseded by IModelDoc2::InsertDome.
Obsolete. Superseded by [IModelDoc2::InsertDome](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertDome.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertDome( _
   ByVal Height As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal DoEllipticSurface As System.Boolean _
) 
```

```

Dim instance As IModelDoc
Dim Height As System.Double
Dim ReverseDir As System.Boolean
Dim DoEllipticSurface As System.Boolean
 
instance.InsertDome(Height, ReverseDir, DoEllipticSurface)
```

```

void InsertDome( 
   System.double Height,
   System.bool ReverseDir,
   System.bool DoEllipticSurface
)
```

```

void InsertDome( 
   System.double Height,
   System.bool ReverseDir,
   System.bool DoEllipticSurface
) 
```

#### Parameters

*Height*

*ReverseDir*

*DoEllipticSurface*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)

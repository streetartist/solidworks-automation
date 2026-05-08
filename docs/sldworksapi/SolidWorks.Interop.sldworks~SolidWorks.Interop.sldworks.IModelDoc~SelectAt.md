# SelectAt Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SelectAt`

Obsolete. Superseded by IModelDoc2::SelectAt.
Obsolete. Superseded by [IModelDoc2::SelectAt](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectAt.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SelectAt( _
   ByVal Flags As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) 
```

```

Dim instance As IModelDoc
Dim Flags As System.Integer
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
 
instance.SelectAt(Flags, X, Y, Z)
```

```

void SelectAt( 
   System.int Flags,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

void SelectAt( 
   System.int Flags,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*Flags*

*X*

*Y*

*Z*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)

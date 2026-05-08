# CreateUnfoldedViewAt2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt2`

Obsolete. Superseded by IDrawingDoc::CreateUnfoldedViewAt3.
Obsolete. Superseded by [IDrawingDoc::CreateUnfoldedViewAt3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateUnfoldedViewAt2( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal NotAligned As System.Boolean _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim NotAligned As System.Boolean
Dim value As System.Boolean
 
value = instance.CreateUnfoldedViewAt2(X, Y, Z, NotAligned)
```

```

System.bool CreateUnfoldedViewAt2( 
   System.double X,
   System.double Y,
   System.double Z,
   System.bool NotAligned
)
```

```

System.bool CreateUnfoldedViewAt2( 
   System.double X,
   System.double Y,
   System.double Z,
   System.bool NotAligned
) 
```

#### Parameters

*X*

*Y*

*Z*

*NotAligned*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)

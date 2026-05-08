# InsertTableAnnotation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertTableAnnotation`

Obsolete. Superseded by IDrawingDoc::InsertTableAnnotation2.
Obsolete. Superseded by [IDrawingDoc::InsertTableAnnotation2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertTableAnnotation2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertTableAnnotation( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal Rows As System.Integer, _
   ByVal Columns As System.Integer _
) As TableAnnotation
```

```

Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim Rows As System.Integer
Dim Columns As System.Integer
Dim value As TableAnnotation
 
value = instance.InsertTableAnnotation(X, Y, AnchorType, Rows, Columns)
```

```

TableAnnotation InsertTableAnnotation( 
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.int Rows,
   System.int Columns
)
```

```

TableAnnotation^ InsertTableAnnotation( 
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.int Rows,
   System.int Columns
) 
```

#### Parameters

*X*

*Y*

*AnchorType*

*Rows*

*Columns*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)

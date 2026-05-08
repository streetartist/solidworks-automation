# CreateAuxiliaryViewAt2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2`

Creates an auxiliary view based on a selected edge in a drawing view.
Creates an auxiliary view based on a selected edge in a drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateAuxiliaryViewAt2( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal NotAligned As System.Boolean, _
   ByVal Label As System.String, _
   ByVal Showarrow As System.Boolean, _
   ByVal Flip As System.Boolean _
) As System.Object
```

```

Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim NotAligned As System.Boolean
Dim Label As System.String
Dim Showarrow As System.Boolean
Dim Flip As System.Boolean
Dim value As System.Object
 
value = instance.CreateAuxiliaryViewAt2(X, Y, Z, NotAligned, Label, Showarrow, Flip)
```

```

System.object CreateAuxiliaryViewAt2( 
   System.double X,
   System.double Y,
   System.double Z,
   System.bool NotAligned,
   System.string Label,
   System.bool Showarrow,
   System.bool Flip
)
```

```

System.Object^ CreateAuxiliaryViewAt2( 
   System.double X,
   System.double Y,
   System.double Z,
   System.bool NotAligned,
   System.String^ Label,
   System.bool Showarrow,
   System.bool Flip
) 
```

#### Parameters

*X*
:   X position for the auxiliary view

*Y*
:   Y position for the auxiliary view

*Z*
:   Z position for the auxiliary view

*NotAligned*
:   True aligns the view from its owner, false does not

*Label*
:   String that holds label of the auxiliary view

*Showarrow*
:   True shows the arrow, false hides the arrow

*Flip*
:   True flips the side shown in the auxiliary view, false does not

#### Return Value

Newly created auxiliary view

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::ICreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAuxiliaryViewAt2.md)  
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.md)  
[IDrawingDoc::CreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3.md)

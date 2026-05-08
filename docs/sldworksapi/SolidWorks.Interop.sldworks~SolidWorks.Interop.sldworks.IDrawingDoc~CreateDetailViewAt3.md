# CreateDetailViewAt3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3`

Obsolete. Superseded by IDrawingDoc::CreateDetailViewAt4.
Obsolete. Superseded by [IDrawingDoc::CreateDetailViewAt4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateDetailViewAt3( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Style As System.Integer, _
   ByVal Scale1 As System.Double, _
   ByVal Scale2 As System.Double, _
   ByVal LabelIn As System.String, _
   ByVal Showtype As System.Integer, _
   ByVal FullOutline As System.Boolean _
) As System.Object
```

```

Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Style As System.Integer
Dim Scale1 As System.Double
Dim Scale2 As System.Double
Dim LabelIn As System.String
Dim Showtype As System.Integer
Dim FullOutline As System.Boolean
Dim value As System.Object
 
value = instance.CreateDetailViewAt3(X, Y, Z, Style, Scale1, Scale2, LabelIn, Showtype, FullOutline)
```

```

System.object CreateDetailViewAt3( 
   System.double X,
   System.double Y,
   System.double Z,
   System.int Style,
   System.double Scale1,
   System.double Scale2,
   System.string LabelIn,
   System.int Showtype,
   System.bool FullOutline
)
```

```

System.Object^ CreateDetailViewAt3( 
   System.double X,
   System.double Y,
   System.double Z,
   System.int Style,
   System.double Scale1,
   System.double Scale2,
   System.String^ LabelIn,
   System.int Showtype,
   System.bool FullOutline
) 
```

#### Parameters

*X*
:   X position for the detail view

*Y*
:   Y position for the detail view

*Z*
:   Z position for the detail view

*Style*
:   Style for the detail view as defined in [swDetViewStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDetViewStyle_e.html)

*Scale1*
:   Scale numerator

*Scale2*
:   Scale denominator

*LabelIn*
:   String for the detail view label

*Showtype*
:   Type of sketch profile for the detail view as defined in [swDetCircleShowType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDetCircleShowType_e.html)

*FullOutline*
:   True shows the full outline of the detail view, false does not

#### Return Value

Detail [view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.md)  
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.md)  
[IDrawingDoc::Create1stAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create1stAngleViews2.md)  
[IDrawingDoc::Create3rdAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.md)  
[IDrawingDoc::CreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.md)  
[IDrawingDoc::CreateDrawViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.md)  
[IDrawingDoc::CreateUnfoldedViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt3.md)  
[IDrawingDoc::ICreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAuxiliaryViewAt2.md)  
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.md)  
[IDrawingDoc::ICreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt4.md)

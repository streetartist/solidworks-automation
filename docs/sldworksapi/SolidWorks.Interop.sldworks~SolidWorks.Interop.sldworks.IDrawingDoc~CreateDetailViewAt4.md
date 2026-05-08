# CreateDetailViewAt4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt4`

Creates a detail view in a drawing document.
Creates a detail view in a drawing document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateDetailViewAt4( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Style As System.Integer, _
   ByVal Scale1 As System.Double, _
   ByVal Scale2 As System.Double, _
   ByVal LabelIn As System.String, _
   ByVal Showtype As System.Integer, _
   ByVal FullOutline As System.Boolean, _
   ByVal JaggedOutline As System.Boolean, _
   ByVal NoOutline As System.Boolean, _
   ByVal ShapeIntensity As System.Integer _
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
Dim JaggedOutline As System.Boolean
Dim NoOutline As System.Boolean
Dim ShapeIntensity As System.Integer
Dim value As System.Object
 
value = instance.CreateDetailViewAt4(X, Y, Z, Style, Scale1, Scale2, LabelIn, Showtype, FullOutline, JaggedOutline, NoOutline, ShapeIntensity)
```

```

System.object CreateDetailViewAt4( 
   System.double X,
   System.double Y,
   System.double Z,
   System.int Style,
   System.double Scale1,
   System.double Scale2,
   System.string LabelIn,
   System.int Showtype,
   System.bool FullOutline,
   System.bool JaggedOutline,
   System.bool NoOutline,
   System.int ShapeIntensity
)
```

```

System.Object^ CreateDetailViewAt4( 
   System.double X,
   System.double Y,
   System.double Z,
   System.int Style,
   System.double Scale1,
   System.double Scale2,
   System.String^ LabelIn,
   System.int Showtype,
   System.bool FullOutline,
   System.bool JaggedOutline,
   System.bool NoOutline,
   System.int ShapeIntensity
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
:   Detail view label

*Showtype*
:   Type of sketch for the detail view as defined in [swDetCircleShowType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDetCircleShowType_e.html)

*FullOutline*
:   True to show a full outline, false to not; valid only if NoOutline is false

*JaggedOutline*
:   True to show a jagged outline, false to not; only valid if NoOutline is false

*NoOutline*
:   True to not show an outline, false to show an outline

*ShapeIntensity*
:   Intensity of jagged outline; valid range is 1 (most) to 5 (least) and only valid if JaggedOutline is true and NoOutline is false

#### Return Value

Detail [view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)

Example

[Create Detail Circle and Detail View (C#)](Create_Detail_Circle_and_Detail_View_Example_CSharp.htm)  
[Create Detail Circle and Detail View (VB.NET)](Create_Detail_Circle_and_Detail_View_Example_VBNET.htm)  
[Create Detail Circle and Detail View (VBA)](Create_Detail_Circle_and_Detail_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::CreateViewport3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.md)  
[IDrawingDoc::Create1stAngleViews2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create1stAngleViews2.md)  
[IDrawingDoc::Create3rdAngleViews2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.md)  
[IDrawingDoc::CreateAuxiliaryViewAt2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.md)  
[IDrawingDoc::CreateDrawViewFromModelView3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.md)  
[IDrawingDoc::CreateUnfoldedViewAt3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt3.md)  
[IDrawingDoc::CreateSectionViewAt5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt5.md)

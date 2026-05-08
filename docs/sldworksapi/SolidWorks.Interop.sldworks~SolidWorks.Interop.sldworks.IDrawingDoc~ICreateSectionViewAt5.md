# ICreateSectionViewAt5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt5`

Creates a section view from the section line up to the specified distance at the specified distance.
Creates a section view from the section line up to the specified distance at the specified distance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateSectionViewAt5( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal SectionLabel As System.String, _
   ByVal Options As System.Integer, _
   ByVal NumExcludedComponents As System.Integer, _
   ByRef ExcludedComponents As System.Object, _
   ByVal SectionDepth As System.Double _
) As View
```

```

Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim SectionLabel As System.String
Dim Options As System.Integer
Dim NumExcludedComponents As System.Integer
Dim ExcludedComponents As System.Object
Dim SectionDepth As System.Double
Dim value As View
 
value = instance.ICreateSectionViewAt5(X, Y, Z, SectionLabel, Options, NumExcludedComponents, ExcludedComponents, SectionDepth)
```

```

View ICreateSectionViewAt5( 
   System.double X,
   System.double Y,
   System.double Z,
   System.string SectionLabel,
   System.int Options,
   System.int NumExcludedComponents,
   ref System.object ExcludedComponents,
   System.double SectionDepth
)
```

```

View^ ICreateSectionViewAt5( 
   System.double X,
   System.double Y,
   System.double Z,
   System.String^ SectionLabel,
   System.int Options,
   System.int NumExcludedComponents,
   System.Object^% ExcludedComponents,
   System.double SectionDepth
) 
```

#### Parameters

*X*
:   x position on the drawing sheet for the center of the section view

*Y*
:   y position on the drawing sheet for the center of the section view

*Z*
:   z position on the drawing sheet for the center of the section view

*SectionLabel*
:   Letter for the label for the section view

*Options*
:   Options that affect the section view as defined in [swCreateSectionViewAtOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateSectionViewAtOptions_e.html)

*NumExcludedComponents*
:   Number of components to exclude from the section view

*ExcludedComponents*
:   Array of components to exclude from the section view

*SectionDepth*
:   Distance from the section line to create the section view

#### Return Value

Section [view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)

Remarks

Before calling this method, select the section line or lines to use as a section line.

This method runs silently; the end-user is not prompted for a label.

Use [IView::IGetSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSection.md) to get the [IDrSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md) object, and use [IDrSection::SetLabel2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetLabel2.md) to set the name for the label, which provides a warning if the name is a duplicate and the standard does not accept duplicate names.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::CreateSectionViewAt5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt5.md)  
[IDrawingDoc::CreateSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionView.md)  
[IDrawingDoc::Create1stAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create1stAngleViews2.md)  
[IDrawingDoc::Create3rdAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.md)  
[IDrawingDoc::CreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.md)  
[IDrawingDoc::CreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3.md)  
[IDrawingDoc::CreateDrawViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.md)  
[IDrawingDoc::CreateFlatPatternViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView3.md)  
[IDrawingDoc::CreateRelativeView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateRelativeView.md)  
[IDrawingDoc::CreateUnfoldedViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt3.md)  
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.md)  
[IDrawingDoc::ICreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAuxiliaryViewAt2.md)  
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.md)  
[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)

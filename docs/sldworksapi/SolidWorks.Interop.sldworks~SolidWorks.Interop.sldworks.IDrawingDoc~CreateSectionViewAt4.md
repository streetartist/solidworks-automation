# CreateSectionViewAt4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4`

Obsolete. Superseded by IDrawingDoc::CreateSectionViewAt5.
Obsolete. Superseded by [IDrawingDoc::CreateSectionViewAt5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt5.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSectionViewAt4( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal SectionLabel As System.String, _
   ByVal Options As System.Integer, _
   ByVal ExcludedComponents As System.Object _
) As View
```

```

Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim SectionLabel As System.String
Dim Options As System.Integer
Dim ExcludedComponents As System.Object
Dim value As View
 
value = instance.CreateSectionViewAt4(X, Y, Z, SectionLabel, Options, ExcludedComponents)
```

```

View CreateSectionViewAt4( 
   System.double X,
   System.double Y,
   System.double Z,
   System.string SectionLabel,
   System.int Options,
   System.object ExcludedComponents
)
```

```

View^ CreateSectionViewAt4( 
   System.double X,
   System.double Y,
   System.double Z,
   System.String^ SectionLabel,
   System.int Options,
   System.Object^ ExcludedComponents
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

*ExcludedComponents*
:   Array of components to exclude from the section view

#### Return Value

Pointer to the newly created [IView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) object

Remarks

Before calling this method, select the section line or the lines to use as a section line.

This method runs silently; the end-user is not prompted for a label.

Use [IView::GetSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSection.md) to get the [IDrSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md) object, and use [IDrSection::SetLabel2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~SetLabel2.md) to set the name for the label, which provides a warning if the name is a duplicate and the standard does not accept duplicate names.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::Create1stAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create1stAngleViews2.md)  
[IDrawingDoc::Create3rdAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.md)  
[IDrawingDoc::CreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.md)  
[IDrawingDoc::CreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3.md)  
[IDrawingDoc::CreateDrawViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.md)  
[IDrawingDoc::CreateFlatPatternViewFromModelView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView2.md)  
[IDrawingDoc::CreateSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionView.md)  
[IDrawingDoc::CreateUnfoldedViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt3.md)  
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.md)  
[IDrawingDoc::ICreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAuxiliaryViewAt2.md)  
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.md)  
[IDrawingDoc::ICreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt4.md)

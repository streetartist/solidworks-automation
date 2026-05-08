# CreateDrawViewFromModelView3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3`

Creates a drawing view on the current drawing sheet using the specified model view.
Creates a drawing view on the current drawing sheet using the specified model view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateDrawViewFromModelView3( _
   ByVal ModelName As System.String, _
   ByVal ViewName As System.String, _
   ByVal LocX As System.Double, _
   ByVal LocY As System.Double, _
   ByVal LocZ As System.Double _
) As View
```

```

Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim ViewName As System.String
Dim LocX As System.Double
Dim LocY As System.Double
Dim LocZ As System.Double
Dim value As View
 
value = instance.CreateDrawViewFromModelView3(ModelName, ViewName, LocX, LocY, LocZ)
```

```

View CreateDrawViewFromModelView3( 
   System.string ModelName,
   System.string ViewName,
   System.double LocX,
   System.double LocY,
   System.double LocZ
)
```

```

View^ CreateDrawViewFromModelView3( 
   System.String^ ModelName,
   System.String^ ViewName,
   System.double LocX,
   System.double LocY,
   System.double LocZ
) 
```

#### Parameters

*ModelName*
:   Full pathname of the model document for which to create the drawing view (see **Remarks**)

*ViewName*
:   Name of the model view from which to create the drawing view (see **Remarks**)

*LocX*
:   x location of drawing view center in meters

*LocY*
:   y location of drawing view center in meters

*LocZ*
:   z location of drawing view center in meters

#### Return Value

Pointer to the newly create [IView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) object

Remarks

This method:

- Places the center of the view at the specified location.
- Uses the [swAutomaticScaling3ViewDrawings](ms-help://SolidWorks.Interop.swconst/SolidWorks/SO_Drawings.htm) setting to set the view scale. If this setting is set to True, then when a new drawing view is inserted, that view automatically scales to fit nicely on the drawing sheet. If there are no views on the sheet, the sheet scale is changed to the appropriate scale, and the view created uses the sheet scale.

If a model document  is currently open in SOLIDWORKS and you don't know its full pathname, call [IModelDoc2::GetPathName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPathName.md) to populate ModelName. Include the **.sldprt** or **.sldasm** extension in the pathname.

ViewName must exactly match the name of the model view. For example, the names of the standard views begin with an asterisk. This asterisk is part of the view name and must be included (for example, "\*Front").

Example

[Insert Model Annotations (C#)](Insert_Model_Annotations_Example_CSharp.htm)  
[Insert Model Annotations (VB.NET)](Insert_Model_Annotations_Example_VBNET.htm)  
[Insert Model Annotations (VBA)](Insert_Model_Annotations_Example_VB.htm)

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
[IDrawingDoc::CreateFlatPatternViewFromModelView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView2.md)  
[IDrawingDoc::CreateSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionView.md)  
[IDrawingDoc::CreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.md)  
[IDrawingDoc::CreateUnfoldedViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt3.md)  
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.md)  
[IDrawingDoc::ICreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAuxiliaryViewAt2.md)  
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.md)  
[IDrawingDoc::ICreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt4.md)  
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.md)

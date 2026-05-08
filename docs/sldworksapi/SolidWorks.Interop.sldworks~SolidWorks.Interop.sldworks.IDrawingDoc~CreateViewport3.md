# CreateViewport3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3`

Creates a an empty view in a drawing.
Creates a an empty view in a drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateViewport3( _
   ByVal LowerLeftX As System.Double, _
   ByVal LowerLeftY As System.Double, _
   ByVal SketchSize As System.Short, _
   ByVal Scale As System.Double _
) As View
```

```

Dim instance As IDrawingDoc
Dim LowerLeftX As System.Double
Dim LowerLeftY As System.Double
Dim SketchSize As System.Short
Dim Scale As System.Double
Dim value As View
 
value = instance.CreateViewport3(LowerLeftX, LowerLeftY, SketchSize, Scale)
```

```

View CreateViewport3( 
   System.double LowerLeftX,
   System.double LowerLeftY,
   System.short SketchSize,
   System.double Scale
)
```

```

View^ CreateViewport3( 
   System.double LowerLeftX,
   System.double LowerLeftY,
   System.short SketchSize,
   System.double Scale
) 
```

#### Parameters

*LowerLeftX*
:   x value for lower-left coordinate for the view

*LowerLeftY*
:   y value for lower-left coordinate for the view

*SketchSize*
:   Approximate number of entries

*Scale*
:   Scale to use for the view

#### Return Value

Pointer to the newly created [IView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) object

Remarks

You cannot set the size of an empty view or resize it. Instead, resizing of the view occurs automatically when you add sketch or model geometry to the view.

The center of the empty view is computed from the specified lower-left corner and default values for the upper-right corner. The latter is set to (0.001, 0.001). The center is computed as follows:

> center = lower-left\_corner + (upper-right\_corner - lower-left\_corner) / 2.0

To move the view, use [IView::Position](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Position.md) or [IView::IPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IPosition.md).

The default SketchSize value is 0. If you are creating more than 500 sketch entities, specify a value instead of using the default.

After you use this method, you can create sketch entities in the new view. One advantage is that users can move the entities around the drawing by dragging the view instead of selecting all the entities.

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
[IDrawingDoc::CreateRelativeView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateRelativeView.md)  
[IDrawingDoc::CreateSectionView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionView.md)  
[IDrawingDoc::CreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.md)  
[IDrawingDoc::CreateUnfoldedViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt3.md)  
[IDrawingDoc::ICreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAuxiliaryViewAt2.md)  
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.md)  
[IDrawingDoc::ICreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt4.md)

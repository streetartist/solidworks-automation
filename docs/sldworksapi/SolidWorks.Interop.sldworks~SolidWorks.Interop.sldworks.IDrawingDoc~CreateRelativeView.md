# CreateRelativeView Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateRelativeView`

Creates a relative drawing view.
Creates a relative drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateRelativeView( _
   ByVal ModelName As System.String, _
   ByVal XPos As System.Double, _
   ByVal YPos As System.Double, _
   ByVal ViewDirFront As System.Integer, _
   ByVal ViewDirRight As System.Integer _
) As View
```

```

Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim XPos As System.Double
Dim YPos As System.Double
Dim ViewDirFront As System.Integer
Dim ViewDirRight As System.Integer
Dim value As View
 
value = instance.CreateRelativeView(ModelName, XPos, YPos, ViewDirFront, ViewDirRight)
```

```

View CreateRelativeView( 
   System.string ModelName,
   System.double XPos,
   System.double YPos,
   System.int ViewDirFront,
   System.int ViewDirRight
)
```

```

View^ CreateRelativeView( 
   System.String^ ModelName,
   System.double XPos,
   System.double YPos,
   System.int ViewDirFront,
   System.int ViewDirRight
) 
```

#### Parameters

*ModelName*
:   Path and filename of the model for which to create a relative drawing view

*XPos*
:   x coordinate where to create the relative drawing view

*YPos*
:   y coordinate where to create a relative drawing view

*ViewDirFront*
:   Orientation as defined by [swRelativeViewCreationDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRelativeViewCreationDirection_e.html)

*ViewDirRight*
:   Orientation as defined by [swRelativeViewCreationDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRelativeViewCreationDirection_e.html)

#### Return Value

[View](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)

Remarks

Select:

- the first orientation component using selection mark 1.
- the second orientation component using selection mark 2.

For multi-body parts only, select bodies to be shown in the created view using selection mark 4.

Example

[Create Relative Drawing View (C#)](Create_Relative_Drawing_View_Example_CSharp.htm)  
[Create Relative Drawing View (VB.NET)](Create_Relative_Drawing_View_Example_VBNET.htm)  
[Create Relative Drawing View (VBA)](Create_Relative_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::CreateDrawViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.md)  
[IDrawingDoc::CreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.md)  
[IDrawingDoc::CreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.md)  
[IDrawingDoc::CreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3.md)  
[IDrawingDoc::Create1stAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create1stAngleViews2.md)  
[IDrawingDoc::Create3rdAngleViews2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~Create3rdAngleViews2.md)  
[IDrawingDoc::ICreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAuxiliaryViewAt2.md)  
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.md)  
[IDrawingDoc::ICreateSectionViewAt4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateSectionViewAt4.md)  
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.md)

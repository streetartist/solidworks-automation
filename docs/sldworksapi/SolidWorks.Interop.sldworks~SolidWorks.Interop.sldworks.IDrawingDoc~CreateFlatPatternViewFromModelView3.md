# CreateFlatPatternViewFromModelView3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView3`

Creates a flat-pattern view from a model view.
Creates a flat-pattern view from a model view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateFlatPatternViewFromModelView3( _
   ByVal ModelName As System.String, _
   ByVal ConfigName As System.String, _
   ByVal LocX As System.Double, _
   ByVal LocY As System.Double, _
   ByVal LocZ As System.Double, _
   ByVal HideBendLines As System.Boolean, _
   ByVal FlipView As System.Boolean _
) As View
```

```

Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim ConfigName As System.String
Dim LocX As System.Double
Dim LocY As System.Double
Dim LocZ As System.Double
Dim HideBendLines As System.Boolean
Dim FlipView As System.Boolean
Dim value As View
 
value = instance.CreateFlatPatternViewFromModelView3(ModelName, ConfigName, LocX, LocY, LocZ, HideBendLines, FlipView)
```

```

View CreateFlatPatternViewFromModelView3( 
   System.string ModelName,
   System.string ConfigName,
   System.double LocX,
   System.double LocY,
   System.double LocZ,
   System.bool HideBendLines,
   System.bool FlipView
)
```

```

View^ CreateFlatPatternViewFromModelView3( 
   System.String^ ModelName,
   System.String^ ConfigName,
   System.double LocX,
   System.double LocY,
   System.double LocZ,
   System.bool HideBendLines,
   System.bool FlipView
) 
```

#### Parameters

*ModelName*
:   Name of model

*ConfigName*
:   Name of configuration

*LocX*
:   X coordinate

*LocY*
:   Y coordinate

*LocZ*
:   Z coordinate

*HideBendLines*
:   True hides bend lines, false does not

*FlipView*
:   True flips the view, false does not

#### Return Value

Flat-pattern [view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)

Example

[Create and Flip Flat-Pattern View of Sheet Metal Part (VBA)](Create_and_Flip_Flat-Pattern_View_of_Sheet_Metal_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IView::FlipView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~FlipView.md)  
[IView::IsFlatPatternView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsFlatPatternView.md)

# FlipView Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~FlipView`

Gets or sets whether to flip a flat-pattern view of a sheet metal part.
Gets or sets whether to flip a flat-pattern view of a sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FlipView As System.Boolean
```

```

Dim instance As IView
Dim value As System.Boolean
 
instance.FlipView = value
 
value = instance.FlipView
```

```

System.bool FlipView {get; set;}
```

```

property System.bool FlipView {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flip the flat-pattern view, false to not

Example

[Create and Flip Flat-Pattern View of Sheet Metal Part (VBA)](Create_and_Flip_Flat-Pattern_View_of_Sheet_Metal_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IDrawingDoc::CreateFlatPatternViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView3.md)

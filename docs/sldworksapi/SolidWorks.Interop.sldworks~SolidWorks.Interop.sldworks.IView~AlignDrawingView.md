# AlignDrawingView Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AlignDrawingView`

Specifies the alignment of this auxiliary drawing view.
Specifies the alignment of this auxiliary drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AlignDrawingView( _
   ByVal AlignViewType As System.Integer _
) As System.Boolean
```

```

Dim instance As IView
Dim AlignViewType As System.Integer
Dim value As System.Boolean
 
value = instance.AlignDrawingView(AlignViewType)
```

```

System.bool AlignDrawingView( 
   System.int AlignViewType
)
```

```

System.bool AlignDrawingView( 
   System.int AlignViewType
) 
```

#### Parameters

*AlignViewType*
:   Type of alignment as defined by [swAlignDrawingViewTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAlignDrawingViewTypes_e.html)

#### Return Value

True if auxiliary drawing view alignment is set, false if not

Example

[Align Auxiliary Drawing View (VBA)](Align_Auxiliary_Drawing_View_Example_VB.htm)  
[Align Auxiliary Drawing View (VB.NET)](Align_Auxiliary_Drawing_View_Example_VBNET.htm)  
[Align Auxiliary Drawing View (C#)](Align_Auxiliary_Drawing_View_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::AlignWithView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AlignWithView.md)  
[IView::GetAlignment Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAlignment.md)  
[IView::RemoveAlignment Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~RemoveAlignment.md)  
[IView::UseDefaultAlignment Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseDefaultAlignment.md)

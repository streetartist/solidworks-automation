# AlignWithView Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AlignWithView`

Sets view alignment.
Sets view alignment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AlignWithView( _
   ByVal AlignType As System.Integer, _
   ByVal BaseView As View _
) As System.Boolean
```

```

Dim instance As IView
Dim AlignType As System.Integer
Dim BaseView As View
Dim value As System.Boolean
 
value = instance.AlignWithView(AlignType, BaseView)
```

```

System.bool AlignWithView( 
   System.int AlignType,
   View BaseView
)
```

```

System.bool AlignWithView( 
   System.int AlignType,
   View^ BaseView
) 
```

#### Parameters

*AlignType*
:   Type of alignment to set as defined by [swAlignViewTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAlignViewTypes_e.html)

*BaseView*
:   [View](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) with which to align, if aligning with another view

#### Return Value

True if view alignment is set, false if not

Remarks

AlignType tells how to align this view.

|  |  |
| --- | --- |
| **If AlignType is set to...** | **Then BaseView...** |
| swAlignViewHorizontalCenter | must be specified as the view with which to align. |
| swAlignViewVerticalCenter | must be specified as the view with which to align. |
| swAlignViewHorizontalOrigin | must be specified as the view with which to align. |
| swAlignViewVerticalOrigin | must be specified as the view with which to align. |
| swNoViewAlignment | is ignored. |
| swDefaultViewAlignment | is ignored. |

Example

[Align Drawing Views (C#)](Align_Drawing_Views_Example_CSharp.htm)  
[Align Drawing Views (VB.NET)](Align_Drawing_Views_Example_VBNET.htm)  
[Align Drawing Views (VBA)](Align_Drawing_Views_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetAlignment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAlignment.md)  
[IView::RemoveAlignment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~RemoveAlignment.md)  
[IView::UseDefaultAlignment Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseDefaultAlignment.md)  
[IView::AlignDrawingView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AlignDrawingView.md)

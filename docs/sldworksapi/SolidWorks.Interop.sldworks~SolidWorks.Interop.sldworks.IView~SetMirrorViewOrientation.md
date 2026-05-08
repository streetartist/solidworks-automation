# SetMirrorViewOrientation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetMirrorViewOrientation`

Sets whether to mirror this view.
Sets whether to mirror this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetMirrorViewOrientation( _
   ByVal BSetIsMirrorView As System.Boolean, _
   ByVal BMirrorVieworientation As System.Integer _
) As System.Boolean
```

```

Dim instance As IView
Dim BSetIsMirrorView As System.Boolean
Dim BMirrorVieworientation As System.Integer
Dim value As System.Boolean
 
value = instance.SetMirrorViewOrientation(BSetIsMirrorView, BMirrorVieworientation)
```

```

System.bool SetMirrorViewOrientation( 
   System.bool BSetIsMirrorView,
   System.int BMirrorVieworientation
)
```

```

System.bool SetMirrorViewOrientation( 
   System.bool BSetIsMirrorView,
   System.int BMirrorVieworientation
) 
```

#### Parameters

*BSetIsMirrorView*
:   True to mirror the view, false to not

*BMirrorVieworientation*
:   Orientation of the mirror view as defined in [swMirrorViewPositions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorViewPositions_e.html)

#### Return Value

True if the method executed successfully, false if not

Example

[Mirror View (C#)](Mirror_View_Example_CSharp.htm)  
[Mirror View (VB.NET)](Mirror_View_Example_VBNET.htm)  
[Mirror View (VBA)](Mirror_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetMirrorViewOrientation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetMirrorViewOrientation.md)

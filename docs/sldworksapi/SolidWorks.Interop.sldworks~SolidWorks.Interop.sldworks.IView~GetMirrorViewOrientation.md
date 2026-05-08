# GetMirrorViewOrientation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetMirrorViewOrientation`

Gets whether this view is mirrored.
Gets whether this view is mirrored.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMirrorViewOrientation( _
   ByRef BIsMirrorView As System.Boolean, _
   ByRef LMirrorViewOrientation As System.Integer _
) As System.Boolean
```

```

Dim instance As IView
Dim BIsMirrorView As System.Boolean
Dim LMirrorViewOrientation As System.Integer
Dim value As System.Boolean
 
value = instance.GetMirrorViewOrientation(BIsMirrorView, LMirrorViewOrientation)
```

```

System.bool GetMirrorViewOrientation( 
   out System.bool BIsMirrorView,
   out System.int LMirrorViewOrientation
)
```

```

System.bool GetMirrorViewOrientation( 
   [Out] System.bool BIsMirrorView,
   [Out] System.int LMirrorViewOrientation
) 
```

#### Parameters

*BIsMirrorView*
:   True if the view is mirrored, false if not

*LMirrorViewOrientation*
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
[IViewe::SetMirrorViewOrientation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetMirrorViewOrientation.md)

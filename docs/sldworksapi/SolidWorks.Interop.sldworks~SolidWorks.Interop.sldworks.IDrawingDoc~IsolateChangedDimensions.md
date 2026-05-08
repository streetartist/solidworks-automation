# IsolateChangedDimensions Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IsolateChangedDimensions`

Isolates changed dimensions.
Isolates changed dimensions.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IsolateChangedDimensions() 
```

```

Dim instance As IDrawingDoc
 
instance.IsolateChangedDimensions()
```

```

void IsolateChangedDimensions()
```

```

void IsolateChangedDimensions(); 
```

Remarks

This method only works with drawings saved in SOLIDWORKS 2012 and later.

To isolate changed dimensions:

1. Call [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.md) and set its UserPreferenceValue argument to swUserPreferenceToggle\_e.swUseChangedDimensions and its OnFlag argument to true.
2. Call IDrawingDoc::IsolateChangedDimensions.

Example

[Isolate Changed Dimension (C#)](Isolate_Changed_Dimension_Example_CSharp.htm)  
[Isolate Changed Dimension (VB.NET)](Isolate_Changed_Dimension_Example_VBNET.htm)  
[Isolate Changed Dimension (VBA)](Isolate_Changed_Dimension_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)

# IGetWeldSymbols Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetWeldSymbols`

Gets all of the weld symbols on this drawing view.
Gets all of the weld symbols on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetWeldSymbols( _
   ByVal NumWeldSymbol As System.Integer _
) As WeldSymbol
```

```

Dim instance As IView
Dim NumWeldSymbol As System.Integer
Dim value As WeldSymbol
 
value = instance.IGetWeldSymbols(NumWeldSymbol)
```

```

WeldSymbol IGetWeldSymbols( 
   System.int NumWeldSymbol
)
```

```

WeldSymbol^ IGetWeldSymbols( 
   System.int NumWeldSymbol
) 
```

#### Parameters

*NumWeldSymbol*
:   Total number of weld symbols on this drawing view

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [weld symbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Remarks

Use this method to obtain the array of weld symbols all at once instead of calling [IView::GetFirstWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstWeldSymbol.md) and then repeatedly calling [IWeldSymbol::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetNext.md) to obtain the weld symbols in the drawing view.

Before calling this method, call [IView::GetWeldSymbolCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldSymbolCount.md) to get the value for numWeldSymbol.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetWeldSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldSymbols.md)

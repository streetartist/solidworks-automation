# IGetDowelSymbols Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDowelSymbols`

Gets all of the dowel symbols on this drawing view.
Gets all of the dowel symbols on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDowelSymbols( _
   ByVal NumDowelSymbol As System.Integer _
) As DowelSymbol
```

```

Dim instance As IView
Dim NumDowelSymbol As System.Integer
Dim value As DowelSymbol
 
value = instance.IGetDowelSymbols(NumDowelSymbol)
```

```

DowelSymbol IGetDowelSymbols( 
   System.int NumDowelSymbol
)
```

```

DowelSymbol^ IGetDowelSymbols( 
   System.int NumDowelSymbol
) 
```

#### Parameters

*NumDowelSymbol*
:   Total number of dowel symbols on this drawing view

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [dowel symbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-Process_methods.htm) for details about this type of method.

Remarks

Use this method to obtain the array of dowel symbols all at once instead of calling [IView::GetFirstDowelSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDowelSymbol.md) and then repeatedly calling [IDowelSymbol::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~GetNext.md) to obtain the remaining dowel symbols on this drawing view.

Before calling this method, call [IView::GetDowelSymbolCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDowelSymbolCount.md) to get the value for numDowelSymbol.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDowelSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDowelSymbols.md)

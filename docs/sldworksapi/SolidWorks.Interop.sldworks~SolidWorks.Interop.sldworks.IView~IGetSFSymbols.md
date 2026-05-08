# IGetSFSymbols Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSFSymbols`

Gets all of the surface finish symbols in this drawing view.
Gets all of the surface finish symbols in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSFSymbols( _
   ByVal NumSFSymbol As System.Integer _
) As SFSymbol
```

```

Dim instance As IView
Dim NumSFSymbol As System.Integer
Dim value As SFSymbol
 
value = instance.IGetSFSymbols(NumSFSymbol)
```

```

SFSymbol IGetSFSymbols( 
   System.int NumSFSymbol
)
```

```

SFSymbol^ IGetSFSymbols( 
   System.int NumSFSymbol
) 
```

#### Parameters

*NumSFSymbol*
:   Total number of surface finish symbols this drawing view

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [surface finish symbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Remarks

Use this method to obtain the array of multi-jog leaders all at once instead of calling [IView::GetFirstSFSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstSFSymbol.md) and then repeatedly calling [ISFSymbol::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetNext.md) to obtain the remaining multi-jog leaders in the drawing view.

Before calling this method, call [IView::GetSFSymbolCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSFSymbolCount.md) to get the value for numSFSymbol.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetSFSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSFSymbols.md)

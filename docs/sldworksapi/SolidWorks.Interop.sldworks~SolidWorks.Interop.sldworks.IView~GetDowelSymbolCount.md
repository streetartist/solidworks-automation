# GetDowelSymbolCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDowelSymbolCount`

Gets the number of dowel symbols in this drawing view.
Gets the number of dowel symbols in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDowelSymbolCount() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.GetDowelSymbolCount()
```

```

System.int GetDowelSymbolCount()
```

```

System.int GetDowelSymbolCount(); 
```

#### Return Value

Number of dowel symbols

Remarks

Call this method before calling [IView::IGetDowelSymbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDowelSymbols.md) to determine the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDowelSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDowelSymbols.md)

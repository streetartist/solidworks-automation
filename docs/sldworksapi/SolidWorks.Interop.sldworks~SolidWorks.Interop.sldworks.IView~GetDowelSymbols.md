# GetDowelSymbols Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDowelSymbols`

Gets all of the dowel symbols on this drawing view.
Gets all of the dowel symbols on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDowelSymbols() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetDowelSymbols()
```

```

System.object GetDowelSymbols()
```

```

System.Object^ GetDowelSymbols(); 
```

#### Return Value

Array of [dowel symbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol.md)

Remarks

Use this method to obtain the array of dowel symbols all at once instead of calling [IView::GetFirstDowelSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDowelSymbol.md) and then repeatedly calling [IDowelSymbol::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~GetNext.md) to obtain the remaining dowel symbols on this drawing view.

Example

[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)  
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)  
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDowelSymbolCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDowelSymbolCount.md)  
[IView::IGetDowelSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDowelSymbols.md)

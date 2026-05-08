# GetWeldSymbols Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldSymbols`

Gets all of the weld symbols on this drawing view.
Gets all of the weld symbols on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetWeldSymbols() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetWeldSymbols()
```

```

System.object GetWeldSymbols()
```

```

System.Object^ GetWeldSymbols(); 
```

#### Return Value

Array of [weld symbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)

Remarks

This method can be used to obtain the array of annotations all at once instead of calling [IView::GetFirstWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstWeldSymbol.md) and then repeatedly calling [IWeldSymbol::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetNext.md) to obtain the annotations.

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
[IView::GetWeldSymbolCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldSymbolCount.md)  
[IView::IGetWeldSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetWeldSymbols.md)

# GetSFSymbols Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSFSymbols`

Gets all of the surface finish symbols in this drawing view.
Gets all of the surface finish symbols in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSFSymbols() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetSFSymbols()
```

```

System.object GetSFSymbols()
```

```

System.Object^ GetSFSymbols(); 
```

#### Return Value

Array of [surface finish symbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)

Remarks

Use this method to obtain the array of surface finish symbols all at once instead of calling [IView::GetFirstSFSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstSFSymbol.md) and then repeatedly calling [ISFSymbol::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetNext.md) to obtain the remaining surface finish symbols in the drawing view.

Example

[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)  
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)  
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetSFSymbolCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSFSymbolCount.md)  
[IView::IGetSFSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSFSymbols.md)

# GetSFSymbolCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSFSymbolCount`

Gets the number of surface finish symbols on this drawing view.
Gets the number of surface finish symbols on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSFSymbolCount() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.GetSFSymbolCount()
```

```

System.int GetSFSymbolCount()
```

```

System.int GetSFSymbolCount(); 
```

#### Return Value

Total number of surface finish symbols on this drawing view

Remarks

Call this method before calling [IView::IGetSFSymbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSFSymbols.md) to determine the size of the array for that method.

Example

[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)  
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)  
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetSFSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSFSymbols.md)

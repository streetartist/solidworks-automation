# IGetFirstSFSymbol Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstSFSymbol`

Gets the first surface-finish symbols in the view.
Gets the first surface-finish symbols in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFirstSFSymbol() As SFSymbol
```

```

Dim instance As IView
Dim value As SFSymbol
 
value = instance.IGetFirstSFSymbol()
```

```

SFSymbol IGetFirstSFSymbol()
```

```

SFSymbol^ IGetFirstSFSymbol(); 
```

#### Return Value

First [surface-finish symbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetFirstSFSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstSFSymbol.md)  
[ISFSymbol::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetNext.md)  
[ISFSymbol::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetNext.md)

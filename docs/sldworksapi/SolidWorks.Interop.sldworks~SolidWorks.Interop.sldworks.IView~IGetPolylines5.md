# IGetPolylines5 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolylines5`

Obsolete. Superseded by IView::GetPolyLines6 and IView::IGetPolyLines6.
Obsolete. Superseded by [IView::GetPolyLines6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetPolylines6.md) and [IView::IGetPolyLines6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetPolylines6.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetPolylines5( _
   ByVal CrossHatchOption As System.Short, _
   ByVal ArraySize As System.Integer _
) As System.Double
```

```

Dim instance As IView
Dim CrossHatchOption As System.Short
Dim ArraySize As System.Integer
Dim value As System.Double
 
value = instance.IGetPolylines5(CrossHatchOption, ArraySize)
```

```

System.double IGetPolylines5( 
   System.short CrossHatchOption,
   System.int ArraySize
)
```

```

System.double IGetPolylines5( 
   System.short CrossHatchOption,
   System.int ArraySize
) 
```

#### Parameters

*CrossHatchOption*

*ArraySize*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)

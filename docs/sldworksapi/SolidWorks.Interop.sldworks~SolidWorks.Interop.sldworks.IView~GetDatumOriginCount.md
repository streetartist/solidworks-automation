# GetDatumOriginCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumOriginCount`

Gets the number of datum origins on this drawing view.
Gets the number of datum origins on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDatumOriginCount() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.GetDatumOriginCount()
```

```

System.int GetDatumOriginCount()
```

```

System.int GetDatumOriginCount(); 
```

#### Return Value

Number of datum origins

Remarks

Call this method before calling [IView::IGetDatumOrigins](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumOrigins.md) to determine the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetDatumOrigins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumOrigins.md)

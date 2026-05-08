# GetFirstDatumOrigin Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDatumOrigin`

Gets the first datum origin in this drawing view.
Gets the first datum origin in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstDatumOrigin() As DatumOrigin
```

```

Dim instance As IView
Dim value As DatumOrigin
 
value = instance.GetFirstDatumOrigin()
```

```

DatumOrigin GetFirstDatumOrigin()
```

```

DatumOrigin^ GetFirstDatumOrigin(); 
```

#### Return Value

First [datum origin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IDatumOrigin::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~GetNext.md)  
[IView::GetDatumOrigins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumOrigins.md)  
[IView::IGetDatumOrigins Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumOrigins.md)

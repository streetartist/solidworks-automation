# GetFirstGTOL Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstGTOL`

Gets the first geometric tolerance in this view.
Gets the first geometric tolerance in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstGTOL() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetFirstGTOL()
```

```

System.object GetFirstGTOL()
```

```

System.Object^ GetFirstGTOL(); 
```

#### Return Value

First [GTol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IGtol::GetNextGTOL Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetNextGTOL.md)  
[IGtol::IGetNextGTOL Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetNextGTOL.md)  
[IView::IGetFirstGTOL Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstGTOL.md)  
[IView::IGetGTols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetGTols.md)  
[IView::GetGTols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetGTols.md)

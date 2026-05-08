# IGetFirstCThread Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstCThread`

Gets the first cosmetic thread in the view.
Gets the first cosmetic thread in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFirstCThread() As CThread
```

```

Dim instance As IView
Dim value As CThread
 
value = instance.IGetFirstCThread()
```

```

CThread IGetFirstCThread()
```

```

CThread^ IGetFirstCThread(); 
```

#### Return Value

First [cosmetic thread](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetFirstCThread Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCThread.md)  
[ICThread::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~GetNext.md)  
[ICThread::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~IGetNext.md)

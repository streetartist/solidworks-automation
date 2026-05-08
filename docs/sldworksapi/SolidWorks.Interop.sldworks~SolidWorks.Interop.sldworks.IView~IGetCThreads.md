# IGetCThreads Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCThreads`

Gets all of the cosmetic threads on this drawing view.
Gets all of the cosmetic threads on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetCThreads( _
   ByVal NumCThread As System.Integer _
) As CThread
```

```

Dim instance As IView
Dim NumCThread As System.Integer
Dim value As CThread
 
value = instance.IGetCThreads(NumCThread)
```

```

CThread IGetCThreads( 
   System.int NumCThread
)
```

```

CThread^ IGetCThreads( 
   System.int NumCThread
) 
```

#### Parameters

*NumCThread*
:   Total number of cosmetic threads on the drawing view

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [cosmetic threads](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Use this method to obtain the array of cosmetic threads all at once instead of calling [IView::GetFirstCThread](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCThread.md) and then repeatedly calling [ICThread::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~GetNext.md) to obtain the remaining cosmetic threads on the drawing view.

Before calling this method, call [IView::GetCThreadCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCThreadCount.md) to get the value for numCThread.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetCThreadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCThreadCount.md)  
[IView::GetCThreads Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCThreads.md)  
[IView::GetFirstCThread Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCThread.md)

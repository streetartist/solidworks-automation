# GetFirstCThread Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCThread`

Gets the first cosmetic thread in the view.
Gets the first cosmetic thread in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstCThread() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetFirstCThread()
```

```

System.object GetFirstCThread()
```

```

System.Object^ GetFirstCThread(); 
```

#### Return Value

First [cosmetic thread](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.md)

Example

[Get Patterned Cosmetic Thread Annotations Data (C#)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_CSharp.htm)  
[Get Patterned Cosmetic Thread Annotations Data (VB.NET)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VBNET.htm)  
[Get Patterned Cosmetic Thread Annotations Data (VBA)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IGetFirstCThread Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstCThread.md)  
[ICThread::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~GetNext.md)  
[ICThread::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~IGetNext.md)  
[IView::IGetCThreads Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCThreads.md)  
[IView::GetCThreads Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCThreads.md)

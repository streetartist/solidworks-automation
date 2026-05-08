# GetCThreads Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCThreads`

Gets all of the cosmetic threads on this drawing view.
Gets all of the cosmetic threads on this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCThreads() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetCThreads()
```

```

System.object GetCThreads()
```

```

System.Object^ GetCThreads(); 
```

#### Return Value

Array of [cosmetic threads](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.md)

Remarks

Use this method to obtain the array of cosmetic threads all at once instead of calling [IView::GetFirstCThread](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCThread.md) and then repeatedly calling [ICThread::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~GetNext.md) to obtain the remaining cosmetic threads on the drawing view.

Example

[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)  
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)  
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetCThreadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCThreadCount.md)  
[IView::IGetCThreads Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCThreads.md)  
[IModelDocExtension::HasLegacyCThreads Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasLegacyCThreads.md)

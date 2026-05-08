# GetMultiJogLeaders Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetMultiJogLeaders`

Gets all of the multi-jog leaders in this drawing view.
Gets all of the multi-jog leaders in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMultiJogLeaders() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetMultiJogLeaders()
```

```

System.object GetMultiJogLeaders()
```

```

System.Object^ GetMultiJogLeaders(); 
```

#### Return Value

Array of [multi-jog leaders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader.md)

Remarks

Use this method to obtain the array of multi-jog leaders all at once instead of calling [IView::GetFirstMultiJogLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstMultiJogLeader.md) and then repeatedly calling [IMultiJogLeader::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetNext.md) to obtain the remaining multi-jog leaders in the drawing view.

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
[IView::GetMultiJogLeaderCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetMultiJogLeaderCount.md)  
[IView::IGetMultiJogLeaders Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetMultiJogLeaders.md)

# IGetMultiJogLeaders Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetMultiJogLeaders`

Gets all of the multi-jog leaders in this drawing view.
Gets all of the multi-jog leaders in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetMultiJogLeaders( _
   ByVal NumMultiJogLeader As System.Integer _
) As MultiJogLeader
```

```

Dim instance As IView
Dim NumMultiJogLeader As System.Integer
Dim value As MultiJogLeader
 
value = instance.IGetMultiJogLeaders(NumMultiJogLeader)
```

```

MultiJogLeader IGetMultiJogLeaders( 
   System.int NumMultiJogLeader
)
```

```

MultiJogLeader^ IGetMultiJogLeaders( 
   System.int NumMultiJogLeader
) 
```

#### Parameters

*NumMultiJogLeader*
:   Number of multi-jog leaders in this drawing view.

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [multi-jog leaders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Remarks

Use this method to obtain the array of multi-jog leaders all at once instead of calling [IView::GetFirstMultiJogLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstMultiJogLeader.md) and then repeatedly calling [IMultiJogLeader::GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetNext.md) to obtain the remaining multi-jog leaders in the drawing view.

Before calling this method, call [IView::GetMultiJogLeaderCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetMultiJogLeaderCount.md) to get the value for numMultiJogLeader.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetMultiJogLeaders Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetMultiJogLeaders.md)

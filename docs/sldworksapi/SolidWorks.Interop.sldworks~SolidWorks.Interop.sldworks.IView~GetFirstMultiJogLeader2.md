# GetFirstMultiJogLeader2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstMultiJogLeader2`

Gets the first multi-jog leader in the view.
Gets the first multi-jog leader in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstMultiJogLeader2() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetFirstMultiJogLeader2()
```

```

System.object GetFirstMultiJogLeader2()
```

```

System.Object^ GetFirstMultiJogLeader2(); 
```

Remarks

This method obsoletes IView::GetFirstMultiJogLeader by supporting inactive sheets.

Example

[Get Multi-jog Leader Data (VBA)](Get_Multi-jog_Leader_Data_Example_VB.htm)  
[Get Multi-jog Leader Data (VB.NET)](Get_Multi-jog_Leader_Data_Example_VBNET.htm)  
[Get Multi-jog Leader Data (C#)](Get_Multi-jog_Leader_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IMultiJogLeader::GetNext Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader~GetNext.md)  
[IView::GetMultiJogLeaders Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetMultiJogLeaders.md)

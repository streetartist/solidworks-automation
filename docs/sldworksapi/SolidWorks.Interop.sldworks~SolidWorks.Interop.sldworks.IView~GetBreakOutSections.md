# GetBreakOutSections Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakOutSections`

Gets all of the broken-out sections in this view.
Gets all of the broken-out sections in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBreakOutSections() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetBreakOutSections()
```

```

System.object GetBreakOutSections()
```

```

System.Object^ GetBreakOutSections(); 
```

#### Return Value

Array of broken-out section [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Example

[Get Broken-Out Section Feature Data (C#)](Get_Broken_Out_Section_Feature_Data_Example_CSharp.htm)  
[Get Broken-Out Section Feature Data (VB.NET)](Get_Broken_Out_Section_Feature_Data_Example_VBNET.htm)  
[Get Broken-Out Section Feature Data (VBA)](Get_Broken_Out_Section_Feature_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IGetBreakOutSections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakOutSections.md)  
[IView::GetBreakOutSectionCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakOutSectionCount.md)

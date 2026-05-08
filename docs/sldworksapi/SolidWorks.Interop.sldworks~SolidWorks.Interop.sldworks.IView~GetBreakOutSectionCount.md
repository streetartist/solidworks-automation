# GetBreakOutSectionCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakOutSectionCount`

Gets the number of broken-out sections in this view.
Gets the number of broken-out sections in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBreakOutSectionCount() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.GetBreakOutSectionCount()
```

```

System.int GetBreakOutSectionCount()
```

```

System.int GetBreakOutSectionCount(); 
```

#### Return Value

Number of broken-out sections

Remarks

Call this method before calling [IView::IGetBreakOutSections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakOutSections.md) to determine the size of the array for that method.

Example

[Get Broken-Out Section Feature Data (VBA)](Get_Broken_Out_Section_Feature_Data_Example_VB.htm)  
[Get Broken-Out Section Feature Data (VB.NET)](Get_Broken_Out_Section_Feature_Data_Example_VBNET.htm)  
[Get Broken-Out Section Feature Data (C#)](Get_Broken_Out_Section_Feature_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetBreakOutSections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakOutSections.md)

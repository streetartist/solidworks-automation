# GetSectionLines Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLines`

Gets the section lines in the view.
Gets the section lines in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSectionLines() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetSectionLines()
```

```

System.object GetSectionLines()
```

```

System.Object^ GetSectionLines(); 
```

#### Return Value

Array of [section lines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)

Remarks

This method returns the section lines regardless if the view is visible. If the view is hidden, the section lines are still returned.

Example

[Get Section View (VBA)](Get_Section_View_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IView::EnumSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines.md)  
[IView::GetSection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSection.md)  
[IView::GetSectionLineCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineCount2.md)  
[IView::GetSectionLineInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineInfo2.md)  
[IView::GetSectionLineStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineStrings.md)  
[IView::IGetSection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSection.md)  
[IView::IGetSectionLineInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLineInfo2.md)  
[IView::IGetSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLines.md)  
[IView::IGetSectionLineStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLineStrings.md)

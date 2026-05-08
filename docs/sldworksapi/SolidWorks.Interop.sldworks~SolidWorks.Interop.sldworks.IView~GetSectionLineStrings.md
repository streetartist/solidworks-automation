# GetSectionLineStrings Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineStrings`

Gets an array of strings; each string represents the text label for a section line in this view.
Gets an array of strings; each string represents the text label for a section line in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSectionLineStrings() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetSectionLineStrings()
```

```

System.object GetSectionLineStrings()
```

```

System.Object^ GetSectionLineStrings(); 
```

#### Return Value

Array of strings with one string for each section line in the view

Remarks

To determine the number of the strings returned, call [IView::GetSectionLineCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineCount2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::EnumSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EnumSectionLines.md)  
[IView::GetSection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSection.md)  
[IView::GetSectionLineInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLineInfo2.md)  
[IView::GetSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSectionLines.md)  
[IView::IGetSection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSection.md)  
[IView::IGetSectionLineInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLineInfo2.md)  
[IView::IGetSectionLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLines.md)  
[IView::IGetSectionLineStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSectionLineStrings.md)
